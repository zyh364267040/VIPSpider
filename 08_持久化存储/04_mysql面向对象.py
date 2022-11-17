# -*- coding = utf-8 -*-
# @Time: 2021/10/20 下午9:54
import pymysql
from pymysql.cursors import DictCursor


class NoDatabaseException(Exception):
    pass


class DBHelper(object):

    def __init__(self, database=None, user='root', password='mysql', host='192.168.203.2', port=3306):
        """初始化,连接到数据库"""
        if database:
            self.conn = pymysql.connect(
                database=database,
                user=user,
                password=password,
                host=host,
                port=port
            )
        else:
            raise NoDatabaseException('没有提供正确的数据库!')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.conn.close()

    def _change(self, sql, *args, isInsert=False):
        # 连接游标
        cursor = self.conn.cursor()
        try:
            # 执行sql
            count = cursor.execute(sql, args)
            # 判断是不是添加数据
            if isInsert:
                new_id = cursor.lastrowid
                # 返回添加数据的编号
                return new_id
            else:
                return count
        except Exception as e:
            print('报错了!', e)
        finally:
            # 关闭游标
            if cursor:
                cursor.close()

    def insert(self, sql, *args):
        """添加数据"""
        return self._change(sql, *args, isInsert=True)

    def update(self, sql, *args):
        """修改数据"""
        return self._change(sql, *args)

    def delete(self, sql, *args):
        """删除数据"""
        return self._change(sql, *args)

    def search_all(self, sql, *args):
        """查询所有数据"""
        # 创建游标
        cursor = self.conn.cursor(cursor=DictCursor)
        try:
            # 执行sql语句
            cursor.execute(sql, args)
            result = cursor.fetchall()
            return result
        finally:
            if cursor:
                cursor.close()

    def search_one(self, sql, *args):
        """查询一条数据"""
        cursor = self.conn.cursor(cursor=DictCursor)
        try:
            cursor.execute(sql, args)
            result = cursor.fetchone()
            return result
        finally:
            if cursor:
                cursor.close()


if __name__ == '__main__':
    with DBHelper('test') as db:
        result = db.search_all('select * from stu')
        print(result)
