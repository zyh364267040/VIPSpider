# -*- coding = utf-8 -*-
# @Time: 2021/10/13 上午12:03
import requests
from lxml import etree
from urllib import parse
import re
import asyncio
import aiohttp
import aiofiles
import os
from Crypto.Cipher import AES


# 获取网页源码数据
def get_page_source(url):
    # 发送请求
    res = requests.get(url)
    res.encoding = 'utf-8'

    return res.text


def get_movie_page_source(url):
    print('开始获取电影页src!', url)
    # 获取网页源码数据
    res_text = get_page_source(url)
    # 解析出电影的src
    tree = etree.HTML(res_text)
    movie_src = tree.xpath('//iframe[@id="mplay"]/@src')[0]
    # 拼接获取到的url连接
    movie_src = parse.urljoin(url, movie_src)

    print('成功获取电影页src!', movie_src)
    return movie_src


def get_first_m3u8(url):
    print('开始获取第一层的m3u8!', url)
    # 获取网页源码数据
    res_text = get_page_source(url)
    # 使用正则获取第一层m3u8文件的url
    obj = re.compile(r'url: "(?P<first_m3u8_url>.*?)",', re.S)
    result = re.search(obj, res_text)
    first_m3u8_url = result.group('first_m3u8_url')

    print('获取第一层的m3u8成功!', first_m3u8_url)
    return first_m3u8_url


def second_m3u8_file(url):
    print('开始获取第二层m3u8文件!', url)
    # 获取网页源码数据
    res_text = get_page_source(url)
    # 从获取到的响应中获取第二层m3u8文件的url
    second_m3u8_url = res_text.split()[-1]
    second_m3u8_url = parse.urljoin(url, second_m3u8_url)
    print('获取第二层m3u8文件url成功!', second_m3u8_url)

    # 获取第二层m3u8文件
    second_m3u8_file_text = get_page_source(second_m3u8_url)
    with open('m3u8.txt', 'w', encoding='utf-8') as f:
        f.write(second_m3u8_file_text)

    print('获取第二层m3u8文件成功!文件名:m3u8.txt')
    return None


def get_ts_file_url_list():
    print('开始获取m3u8文件的url')
    f = open('m3u8.txt', 'r', encoding='utf-8')
    # 存储ts文件url的列表
    ts_url_list = []
    # 逐行取出文件内容
    for line in f:
        # 如果内容第一个为 # 跳过
        if line.startswith('#'):
            continue
        # 去掉连接中的换行符
        ts_url = line.strip()
        ts_url_list.append(ts_url)

    print('获取m3u8文件的url成功', ts_url_list)
    return ts_url_list


async def download_one_ts(url):
    # 自省
    for i in range(10):
        try:
            print('开始下载:', url)
            # ts文件名称
            file_name = url.split('/')[-1]
            # 创建请求对象
            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
                # 发送请求,获取响应
                async with session.get(url) as res:
                    # 获取ts文件内容
                    ts_content = await res.content.read()
                    # 判断保存ts的文件夹是否存在,不存在创建
                    if not os.path.exists('ts文件'):
                        os.mkdir('ts文件')
                    # 把ts内容写入到ts文件中
                    async with aiofiles.open(f'./ts文件/{file_name}', 'wb') as f:
                        await f.write(ts_content)
            print('下载完毕:', url)
            break
        except:
            print(f'重新下载第{i+1}次:', url)


async def download_all_ts(ts_url_list):
    print('开始下载电影ts文件!')
    # 从m3u8文件中取出文件内容
    tasks = []
    # 循环取出ts_url
    for ts_url in ts_url_list:
        # 每个连接加入任务队列
        task = asyncio.create_task(download_one_ts(ts_url))
        tasks.append(task)

    await asyncio.wait(tasks)


def get_key():
    print('开始获取key!')
    # 读取m3u8文件
    with open('m3u8.txt', 'r', encoding='utf-8') as f:
        # 使用正则获取m3u8文件中key的url
        obj = re.compile(r'URI="(?P<key_url>.*?)"', re.S)
        result = re.search(obj, f.read())
        key_url = result.group('key_url')

    # 发送请求获取key
    key = get_page_source(key_url)

    print('获取key成功!')
    return key.encode('utf-8')


async def dec_one_ts_file(ts_file_name, key):
    print('即将开始解密!', ts_file_name)
    if not os.path.exists('ts文件解密后'):
        os.mkdir('ts文件解密后')
    # 加密解密对象创建
    aes = AES.new(key=key, IV=b'0000000000000000', mode=AES.MODE_CBC)
    async with aiofiles.open(f'./ts文件/{ts_file_name}', 'rb') as f1, \
            aiofiles.open(f'./ts文件解密后/{ts_file_name}', 'wb') as f2:
        # 从加密文件中读出内容
        ts_content = await f1.read()
        # 解密文件
        ts_content = aes.decrypt(ts_content)
        # 保存解密后的文件
        await f2.write(ts_content)
    print('解密完成!', ts_file_name)


async def dec_all_ts_file(ts_url_list, key):
    print('开始解析ts文件!')
    tasks = []
    # 从ts文件列表中取出每个ts文件的url
    for ts_url in ts_url_list:
        # 获取ts文件的后缀名称
        ts_file_name = ts_url.split('/')[-1]
        # 创建协程任务
        task = asyncio.create_task(dec_one_ts_file(ts_file_name, key))
        tasks.append(task)

    await asyncio.wait(tasks)


def merge_ts_file(ts_url_list):
    print('开始合并ts文件!')
    # 存储文件名字
    name_list = []
    for ts_url in ts_url_list:
        file_name = ts_url.split('/')[-1]
        name_list.append(file_name)

    # 记录当前目录
    now_dir = os.getcwd()
    # 进入到解密后的ts文件目录内
    os.chdir('./ts文件解密后')

    merge_name_list = []
    n = 1
    for i in range(len(name_list)):
        ts_name = name_list[i]
        merge_name_list.append(ts_name)
        # 每100个ts文件合并成一个ts文件
        if (i / 100 == 0) and (i != 0):
            ts_name_str = ' '.join(merge_name_list)
            os.system(f'cat {ts_name_str} > {n}.ts')
            n += 1
            merge_name_list = []
    # 把最后没有合并的合并
    ts_name_str = ' '.join(merge_name_list)
    os.system(f'cat {ts_name_str} > {n}.ts')

    # 把合并后的文件,再次进行合并成一个mp4文件
    merge_name_list = []
    for i in range(1, n+1):
        merge_name_list.append(f'{i}.ts')

    # 把合并完的文件,最终合并为一个电影文件
    ts_name_str = ' '.join(merge_name_list)
    os.system(f'cat {ts_name_str} > ../中国医生.mp4')

    # 合并完成后,回到上一层文件目录
    os.chdir(now_dir)
    print('合并文件完成!')


def main():
    # 电影起始的url
    url = 'http://www.wbdy.tv/play/43938_1_1.html'
    # 1.发送请求,获取电影页面的源码,解析出第一层m3u8文件src
    movie_src = get_movie_page_source(url)
    # 2.从源码中获取第一层m3u8文件
    first_m3u8_url = get_first_m3u8(movie_src)
    # 3.从第一层m3u8文件中获取第二层m3u8文件
    second_m3u8_file(first_m3u8_url)
    # 4.按照第二层m3u8文件,下载电影ts文件
    # 从m3u8文件中取出需要下载ts文件的url
    ts_url_list = get_ts_file_url_list()
    asyncio.run(download_all_ts(ts_url_list))
    # 5.解密ts文件
    # 获取秘钥key
    key = get_key()
    asyncio.run(dec_all_ts_file(ts_url_list, key))
    # 6.合并ts文件
    merge_ts_file(ts_url_list)


if __name__ == '__main__':
    main()
