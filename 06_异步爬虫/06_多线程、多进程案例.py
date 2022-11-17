# -*- coding = utf-8 -*-
# @Time: 2021/10/4 上午10:10
"""
分析:
    进程1:从主页面当中解析出详情页的url,从详情页中提取到图片的下载地址
    进程2:把拿到的下载地址,进行下载
    队列:可以进行进程之间的通信
"""
from multiprocessing import Process, Queue
import requests
from lxml import etree
from urllib import parse
from concurrent.futures import ThreadPoolExecutor


def get_img_src(q):
    url = 'http://www.591mm.com/bztp/dnbz/2.html'
    res = requests.get(url)
    res.encoding = 'utf-8'
    tree = etree.HTML(res.text)
    href_list = tree.xpath('//div[@class="MeinvTuPianBox"]/ul/li/a[1]/@href')
    for href in href_list:
        href = parse.urljoin(url, href)
        child_res = requests.get(href)
        child_res.encoding = 'utf-8'
        child_tree = etree.HTML(child_res.text)
        src = child_tree.xpath('//div[@id="picBody"]//a/img/@src')[0]
        q.put(src)
    q.put('已完成')


def download(url):
    print('开始下载', url)
    name = url.split('/')[-1]
    res = requests.get(url)
    with open('./img/'+name, 'wb') as f:
        f.write(res.content)
    print('下载完毕', url)


def download_img(q):
    with ThreadPoolExecutor(5) as t:
        while True:
            src = q.get()
            if src == '已完成':
                break
            t.submit(download, src)


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=get_img_src, args=(q,))
    p2 = Process(target=download_img, args=(q,))

    p1.start()
    p2.start()
