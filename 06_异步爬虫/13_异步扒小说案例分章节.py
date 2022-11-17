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
    # 解析每一章节名称和url
    tree = etree.HTML(res.text)
    span_list = tree.xpath('//div[@class="booklist clearfix"]/span')

    # 存储整本书每一章节
    book_dict = {}
    # 存储每一章节内小节url
    every_chapter_href = []
    for span in span_list:
        # 解析章节名称
        chapter_title = span.xpath('./text()')[0]
        # 如果为空则取每小节的href
        if chapter_title == ' ':
            chapter_href = span.xpath('./a/@href')[0]
            # 把href添加到准备好的列表
            every_chapter_href.append(chapter_href)
        else:
            # 重置列表
            every_chapter_href = []
            # 把列表赋值给每一章名称上,保存到字典中
            book_dict[chapter_title] = every_chapter_href

    return book_dict


async def download_one(book_chapter, href):
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
            # 文件保存的文件夹
            file_path = f'./明朝那些事儿/{book_chapter}'
            if not os.path.exists(file_path):
                os.mkdir(file_path)
            # 创建文件,写入内容
            async with aiofiles.open(f'{file_path}/{title}.txt', 'w', encoding='utf-8') as f:
                await f.write(content)
    print('下载完成:', href)


async def download(book_dict):
    tasks = []
    # 从字典中获取每一章节
    for book_chapter in book_dict:
        # 获取每一章节内小节的href
        print('开始下载:', book_chapter)
        for href in book_dict[book_chapter]:
            # task = asyncio.create_task(download_one(href))  # py3.6 不能用
            # 把每个任务加入任务列表
            tasks.append(download_one(book_chapter, href))
        print('下载完成:', book_chapter)

    # 等待运行任务列表
    await asyncio.wait(tasks)


def main():
    # 开始的url
    url = 'https://zanghaihua.org/mingchaonaxieshier/'
    # 获取每一章节的url
    book_dict = get_every_page_url(url)
    print('href_list 获取成功!')

    # 使用异步,获取小说每一章节内容
    # asyncio.run(download(book_dict))  # py3.6 不能用
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(download(book_dict))


if __name__ == '__main__':
    main()
