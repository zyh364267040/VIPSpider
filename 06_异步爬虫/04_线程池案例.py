# -*- coding = utf-8 -*-
# @Time: 2021/9/30 下午12:21
import requests
from concurrent.futures import ThreadPoolExecutor


def download(url, data):
    resp = requests.post(url, data=data)
    resp_dict = resp.json()
    resp_list = resp_dict['list']
    for resp_single in resp_list:
        vga_single_list = []

        vga_single_list.append(str(resp_single['id']))
        vga_single_list.append(resp_single['prodName'])
        vga_single_list.append(resp_single['prodCat'])
        vga_single_list.append(resp_single['lowPrice'])
        vga_single_list.append(resp_single['highPrice'])
        vga_single_list.append(resp_single['avgPrice'])
        vga_single_list.append(resp_single['place'])
        vga_single_list.append(resp_single['unitInfo'])
        vga_single_list.append(resp_single['pubDate'])

        vga_str = ",".join(vga_single_list)
        f.write(vga_str + '\n')


if __name__ == '__main__':
    url = 'http://xinfadi.com.cn/getPriceData.html'
    f = open('vga.csv', 'w')

    with ThreadPoolExecutor(2) as t:
        for page in range(1, 5):
            data = {
                'limit': 20,
                'current': page,
                'pubDateStartTime': '',
                'pubDateEndTime': '',
                'prodPcatid': '',
                'prodCatid': '',
                'prodName': '',
            }
            t.submit(download, url, data)

    f.close()
