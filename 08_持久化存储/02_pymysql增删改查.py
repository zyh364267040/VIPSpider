# -*- coding = utf-8 -*-
# @Time: 2021/10/20 下午4:37
import pymysql
from pymysql.cursors import DictCursor


def get_conn():
    """创建连接"""
    conn = pymysql.connect(
        user='root',
        password='mysql',
        port=3306,
        host='192.168.203.2',
        database='test'
    )

    return conn


def change(sql, isInsert = False):
    try:
        # 创建连接
        conn = get_conn()
        # 创建游标
        cursor = conn.cursor()
        # 执行sql语句
        count = cursor.execute(sql)
        # 提交
        conn.commit()
        if isInsert:
            new_id = cursor.lastrowid
            return new_id
        else:
            return count
    except Exception as e:
        print(e)
        # 数据回滚
        conn.rollback()
    finally:
        # 关闭游标
        if cursor:
            cursor.close()
        # 关闭连接
        if conn:
            conn.close()


def add(sql):
    """新增数据"""
    return change(sql, isInsert=True)


def upd(sql):
    """修改数据"""
    return change(sql)


def delete(sql):
    """删除数据"""
    return change(sql)


def search_one(sql):
    """查询一个"""
    try:
        # 创建连接
        conn = get_conn()
        # 创建游标
        cursor = conn.cursor(cursor=DictCursor)
        # 执行sql语句
        cursor.execute(sql)
        # 从游标中获取数据
        result = cursor.fetchone()
        return result
    except Exception as e:
        print(e)
    finally:
        # 关闭游标
        if cursor:
            cursor.close()
        # 关闭连接
        if conn:
            conn.close()


def search_all(sql):
    """查询所有"""
    try:
        # 创建连接
        conn = get_conn()
        # 创建游标
        cursor = conn.cursor(cursor=DictCursor)
        # 执行sql语句
        cursor.execute(sql)
        # 从游标中获取数据
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(e)
    finally:
        # 关闭游标
        if cursor:
            cursor.close()
        # 关闭连接
        if conn:
            conn.close()


if __name__ == '__main__':
    # 新增数据
    # sql = 'insert into stu(sname, sgender, sage, score, class) value("娃哈哈", 1, 18, 88, "三年七班")'
    # ret = add(sql)
    # print(ret)

    # 修改数据
    # sql = 'update stu set sname = "嘻哈哈" where sno = 14'
    # ret = upd(sql)
    # print(ret)

    # 删除数据
    # sql = 'delete from stu where sno = 13'
    # ret = delete(sql)
    # print(ret)

    # 查询一条数据
    # sql = 'select * from stu where sno = 9'
    # result = search_one(sql)
    # print(result)

    # 查询所有数据
    sql = 'select * from stu'
    result = search_all(sql)
    print(result)
