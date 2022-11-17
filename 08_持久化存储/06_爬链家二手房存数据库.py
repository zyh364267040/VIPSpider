# -*- coding = utf-8 -*-
# @Time: 2021/10/26 下午10:03
import requests
from lxml import etree
from pymongo import MongoClient
import pymysql


def get_page_source(url):
    """网页请求,获取响应"""
    res = requests.get(url)

    print('获取数据页面成功!')
    return res.text


def parse_data(html):
    """解析数据,获取二手房信息"""
    tree = etree.HTML(html)
    li_list = tree.xpath('//ul[@class="sellListContent"]/li')
    # 房子信息列表
    page_house_info = []
    for li in li_list:
        # 房子标题
        title = li.xpath('./div[1]/div[1]/a/text()')[0]
        # 房子地址
        flood = '-'.join(li.xpath('./div[1]/div[2]/div[1]/a/text()')).replace(' ', '')
        # 房子信息
        house_info = li.xpath('./div[1]/div[3]/div/text()')[0].split(' | ')
        if len(house_info) == 6:
            house_info.insert(5, '')
        huxing, mianji, chaoxiang, zhuangxiu, louceng, nianfen, yangshi = house_info
        # 房子标签
        tag = li.xpath('./div[1]/div[5]//text()')
        house_dict = {
            'title': title,
            'flood': flood,
            'huxing': huxing,
            'mianji': mianji,
            'chaoxiang': chaoxiang,
            'zhuangxiu': zhuangxiu,
            'louceng': louceng,
            'nianfen': nianfen,
            'yangshi': yangshi,
            'tag': tag
        }
        page_house_info.append(house_dict)

    print('获取房子信息成功!')
    return page_house_info


def save_mongodb(data):
    """将爬取到的房子信息寸到mongodb数据库中"""
    client = MongoClient(port=27017, host='localhost')  # 此处是在Ubuntu中运行,所以用的是localhost
    db = client['ershoufang']
    db['ershoufang'].insert(data)
    print('插入数据完成!')


def save_mysql(data):
    """将爬取到的房子信息寸到mysql数据库中"""
    # 将数据转化成需要的样式
    for house_dict in data:
        house_dict['tag'] = ','.join(house_dict['tag'])
    data_list = [tuple(house_dict.values()) for house_dict in data]

    try:
        # 创建MySQL连接
        conn = pymysql.connect(port=3306, host='192.168.203.3', user='root', password='mysql', database='spider')
        print('数据库连接成功')
        # 创建游标
        cursor = conn.cursor()

        sql = 'insert into ershoufang(title, flood, huxing, mianji, chaoxiang, zhuangxiu, louceng, nianfen, yangshi, tag) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        # cursor.execute(sql)
        cursor.executemany(sql, data_list)
        conn.commit()
        print('数据保存到MySQL成功!')
    except Exception as e:
        print(e)
        conn.rollback()
        print('数据保存到MySQL失败!')
        print(e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print('数据库连接关闭!')


def run():
    for i in range(1, 31):
        url = f'https://bj.lianjia.com/ershoufang/pg{i}/'
        # 获取页面响应数据
        res_text = get_page_source(url)
        # 获取房子信息
        page_house_info = parse_data(res_text)
        # 保存到mongodb数据库
        # save_mongodb(page_house_info)
        # 保存到mysql数据库
        save_mysql(page_house_info)
        break


if __name__ == '__main__':
    run()
