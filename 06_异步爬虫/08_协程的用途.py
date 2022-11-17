# -*- coding = utf-8 -*-
# @Time: 2021/10/7 上午10:56
import asyncio


async def func1():
    print('我是func1')
    await asyncio.sleep(1)
    print('func1结束')


async def func2():
    print('我是func2')
    await asyncio.sleep(2)
    print('func2结束')


async def func3():
    print('我是func3')
    await asyncio.sleep(3)
    print('func3结束')


if __name__ == '__main__':
    f1 = func1()
    f2 = func2()
    f3 = func3()

    tasks = [
        f1,
        f2,
        f3
    ]

    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(asyncio.wait(tasks))
