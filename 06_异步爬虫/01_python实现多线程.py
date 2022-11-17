# -*- coding = utf-8 -*-
# @Time: 2021/9/28 下午10:16
from threading import Thread


def func(name):
    for i in range(1000):
        print(name, i)


if __name__ == '__main__':
    t1 = Thread(target=func, args=('周杰伦',))
    t2 = Thread(target=func, args=('周润发',))
    t3 = Thread(target=func, args=('周星驰',))

    t1.start()
    t2.start()
    t3.start()
    func('周冬雨')
