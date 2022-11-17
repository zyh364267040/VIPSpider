# -*- coding = utf-8 -*-
# @Time: 2021/11/5 下午7:15
from flask import Flask


app = Flask(__name__)


@app.route('/')
def first():
    print('访问根路径')
    return '访问的是根路径'


if __name__ == '__main__':
    app.run()
