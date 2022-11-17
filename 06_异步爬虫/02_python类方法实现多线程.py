# -*- coding = utf-8 -*-
# @Time: 2021/9/28 下午10:22
from threading import Thread


class MyThread(Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    def run(self) -> None:
        for i in range(1000):
            print(f'我爱{self.name}', i)


if __name__ == '__main__':
    t1 = MyThread('周杰伦')
    t2 = MyThread('周润发')
    t3 = MyThread('周星驰')

    t1.start()
    t2.start()
    t3.start()

    MyThread('周冬雨').run()
