# -*- coding = utf-8 -*-
# @Time: 2021/9/29 下午11:24
from concurrent.futures import ThreadPoolExecutor
import time


# def func(name):
#     for i in range(10):
#         print(name, i)
#
#
# if __name__ == '__main__':
#     # with ThreadPoolExecutor(10) as t:
#     #     t.submit(func, '周')
#     #     t.submit(func, '王')
#     #     t.submit(func, '孙')
#
#     with ThreadPoolExecutor(10) as t:
#         for i in range(100):
#             t.submit(func, f'周{i}')


def func(name, t):
    time.sleep(t)
    print(f'我是{name}')
    return name


def fn(res):
    print(res.result())


if __name__ == '__main__':
    # with ThreadPoolExecutor(3) as t:
    #     t.submit(func, '周杰伦', 2).add_done_callback(fn)
    #     t.submit(func, '王力宏', 1).add_done_callback(fn)
    #     t.submit(func, '周润发', 3).add_done_callback(fn)

    with ThreadPoolExecutor(3) as t:
        result = t.map(func, ['周杰伦', '王力宏', '周润发'], [2, 1, 3])

    for r in result:
        print(r)
