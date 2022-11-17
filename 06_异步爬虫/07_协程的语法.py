# -*- coding = utf-8 -*-
# @Time: 2021/10/6 下午12:22
import asyncio


async def func():
    print('我是函数')


if __name__ == '__main__':
    f = func()
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(f)
    # asyncio.run(f)
