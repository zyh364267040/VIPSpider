# -*- coding = utf-8 -*-
# @Time: 2021/10/8 下午9:03
import asyncio
import aiohttp
import aiofiles


async def download(url):
    print('开始下载', url)
    file_name = './asyncio_img/' + url.split('/')[-1]
    async with aiohttp.ClientSession() as session:
        # 发送请求
        async with session.get(url) as res:
            content = await res.content.read()

            # 保存文件
            async with aiofiles.open(file_name, 'wb') as f:
                await f.write(content)

    print('下载结束', url)


async def main():
    url_list = [
        'http://pic3.hn01.cn/wwl/upload/2021/09-20/mtwolicsi5f.jpg',
        'http://pic3.hn01.cn/wwl/upload/2021/09-20/qa00dkkf2ch.jpg',
        'http://pic3.hn01.cn/wwl/upload/2021/08-03/pscvq2vdubd.jpg',
        'http://pic3.hn01.cn/wwl/upload/2021/08-03/ifythfsqbba.jpg'
    ]

    tasks = []
    # 循环取出url
    for url in url_list:
        # create_task() py3.6没有这个
        # task = asyncio.create_task(download(url))
        task = download(url)
        tasks.append(task)

    await asyncio.wait(tasks)


if __name__ == '__main__':
    # asyncio.run(main())

    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())
