# -*- coding = utf-8 -*-
# @Time: 2021/10/9 下午9:56
import requests
from lxml import etree
import asyncio
import aiohttp
import aiofiles
import os


def get_every_page_url(url):
    # 发送请求
    res = requests.get(url)
    print('请求成功!', url)
    # 获取每一个章节的url
    tree = etree.HTML(res.text)
    href_list = tree.xpath('//div[@class="booklist clearfix"]/span/a/@href')
    return href_list


async def download_one(href):
    print('开始下载:', href)
    # 创建异步session
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        # 发送请求
        async with session.get(href) as res:
            # 获取页面HTML
            page_source = await res.text()
            # 解析小说标题和内容
            tree = etree.HTML(page_source)
            title = tree.xpath('//div[@class="chaptertitle clearfix"]/h1/text()')[0]
            content = '\n'.join(tree.xpath('//div[@class="bookcontent clearfix"]/text()')).replace('\u3000', '')

            # 判断文件夹是否存在
            if not os.path.exists('./明朝那些事儿'):
                os.mkdir('./明朝那些事儿')
            # 创建文件,写入内容
            async with aiofiles.open(f'./明朝那些事儿/{title}.txt', 'w', encoding='utf-8') as f:
                await f.write(content)
    print('下载完成:', href)


async def download(href_list):
    tasks = []
    for href in href_list:
        # task = asyncio.create_task(download_one(href))  # py3.6 不能用
        # 把每个任务加入任务列表
        tasks.append(download_one(href))

    # 等待运行任务列表
    await asyncio.wait(tasks)


def main():
    # 开始的url
    url = 'https://zanghaihua.org/mingchaonaxieshier/'
    # 获取每一章节的url
    href_list = get_every_page_url(url)
    print('href_list 获取成功!')
    # 使用异步,获取小说每一章节内容
    # asyncio.run(download(href_list))  # py3.6 不能用
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(download(href_list))


if __name__ == '__main__':
    main()
