# -*- coding = utf-8 -*-
# @Time: 2021/10/18 下午8:18
import pymysql


if __name__ == '__main__':
    try:
        # 1.创建连接
        conn = pymysql.connect(
            user='root',
            password='mysql',
            port=3306,
            host='192.168.203.2',
            database='test'
        )

        # 目标:执行sql语句
        # 2.创建游标
        cursor = conn.cursor()

        # 3.准备sql语句
        sql = 'insert into stu(sname, sage, score, sgender, class) value ("王老五", 55, 45, 1, "三年一班")'

        # 4.执行sql语句
        result = cursor.execute(sql)
        print(result)

        # pymysql 在执行sql的时候,默认开启了事物
        # 5.提交事务
        conn.commit()
    except:
        # 回滚
        conn.rollback()
    finally:
        # 最终关闭数据库连接
        if conn:
            conn.close()
