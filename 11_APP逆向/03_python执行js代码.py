# -*- coding = utf-8 -*-
# @Time: 2022/5/28 下午4:10
# pip install PyExecJS==1.5.1
import execjs


def main():
    javascript_file = execjs.compile('''
    function createDc() {
        return Math.random();
    }
    ''')
    result = javascript_file.call('createDc')
    print(result)


if __name__ == '__main__':
    main()
