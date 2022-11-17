# -*- coding = utf-8 -*-
# @Time: 2021/10/4 上午9:32
from multiprocessing import Process


def func(name):
    for i in range(1000):
        print(name, i)


if __name__ == '__main__':
    p1 = Process(target=func, args=('周杰伦',))
    p2 = Process(target=func, args=('周润发',))

    p1.start()
    p2.start()
