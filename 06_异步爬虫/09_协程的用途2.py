# -*- coding = utf-8 -*-
# @Time: 2021/10/7 下午9:30
import asyncio


async def download(url, t):
    print('我要开始下载了')
    await asyncio.sleep(t)
    print('我下载完了')


async def main():
    urls = [
        'www.baidu.com',
        'www.sogou.com',
        'www.google.cn'
    ]

    # 需要封装任务列表
    tasks = []
    for url in urls:
        # 创建任务
        # task = asyncio.create_task(download(url, 3))
        # 把任务扔到列表,为了统一处理
        # tasks.append(task)
        tasks.append(download(url, 3))

    # 统一等到协程任务执行完毕
    await asyncio.wait(tasks)


if __name__ == '__main__':
    # asyncio.run(main())

    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())
