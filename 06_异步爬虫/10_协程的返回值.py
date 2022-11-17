# -*- coding = utf-8 -*-
# @Time: 2021/10/7 下午9:59
import asyncio


async def func1():
    print('我是func1')
    await asyncio.sleep(1)
    print('func1结束')
    return 'func1'


async def func2():
    print('我是func2')
    await asyncio.sleep(2)
    print('func2结束')
    return 'func2'


async def func3():
    print('我是func3')
    await asyncio.sleep(3)
    print('func3结束')
    return 'func3'


async def main():
    f1 = func1()
    f2 = func2()
    f3 = func3()

    tasks = [
        # asyncio.create_task(f1),
        # asyncio.create_task(f2),
        # asyncio.create_task(f3),
        f1,
        f2,
        f3
    ]

    # asyncio.wait() 返回的结果,没有顺序
    # 结束, 运行     set集合:无序
    # done, pending = await asyncio.wait(tasks)
    #
    # for t in done:
    #     print(t.result())
    #
    # print(pending)

    # gather 和 wait的区别:gather返回值是有顺序的(按照添加任务的顺序返回的)的
    # return_exceptions=True 如果有错误信息,返回错误信息,其他任务正常执行
    # return_exceptions=False 如果有错误信息,所以任务直接停止

    result = await asyncio.gather(*tasks, return_exceptions=True)
    print(result)


if __name__ == '__main__':
    # asyncio.run(main())

    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())
