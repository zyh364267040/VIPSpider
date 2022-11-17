# -*- coding = utf-8 -*-
# @Time: 2021/10/20 下午5:27
import pymysql
from pymysql.cursors import DictCursor


if __name__ == '__main__':
    conn = pymysql.connect(
        user='root',
        password='mysql',
        port=3306,
        host='192.168.203.2',
        database='test'
    )

    cursor = conn.cursor(cursor=DictCursor)

    sql = 'select * from stu'

    ret = cursor.execute(sql)

    # one = cursor.fetchone()
    # print(one)
    #
    # one = cursor.fetchone()
    # print(one)
    #
    # one = cursor.fetchone()
    # print(one)
    #
    # one = cursor.fetchone()
    # print(one)

    # all = cursor.fetchall()
    # print(all)

    many = cursor.fetchmany(3)
    print(many)
