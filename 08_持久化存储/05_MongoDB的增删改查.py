# -*- coding = utf-8 -*-
# @Time: 2021/10/23 上午8:11
from pymongo import MongoClient


def get_db():
    client = MongoClient(host='localhost', port=27017)  # 默认端口号27017
    # 使用stu数据库
    db = client['stu']  # use stu
    return db


def add_one(collection_name, data):
    # 获取db
    db = get_db()
    # result = db['teacher'].insert({'name': '孔子', 'age': 3050})
    # result = db.teacher.insert({'name': '孔子', 'age': 3050})
    # result = db.collection_name.insert({'name': '孔子', 'age': 3050})  # 不能这样写
    result = db[collection_name].insert({'name': '孔子', 'age': 3050})
    print(result)
    return result


def add_many(collection_name, data):
    # 获取db
    db = get_db()
    result = db[collection_name].insert(data)
    print(result)
    return result


def upd(collection_name, condition, prepare):
    db = get_db()
    result = db[collection_name].update(condition, prepare, multi=True)
    print(result)
    return result


def delete(collection_name, condition):
    db = get_db()
    result = db[collection_name].delete_many(condition)
    print(result)


def query(collection_name, condition):
    db = get_db()
    result = db[collection_name].find(condition)
    print(result)
    return list(result)


if __name__ == '__main__':
    # add_one()
    # add_many('teacher', [{'name': '孟子', 'age': 3000}, {'name': '荀子', 'age': 2950}])
    # upd('teacher', {'name': '孔子'}, {'$set': {'age': 3070}})
    # delete('teacher', {'name': '荀子'})
    res = query('teacher', {'name': {'$regex': '.*子'}})
    print(res)
