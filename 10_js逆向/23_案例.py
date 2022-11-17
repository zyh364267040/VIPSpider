# -*- coding = utf-8 -*-
# @Time: 2021/11/9 下午6:49
import requests
from Crypto.Cipher import DES
import binascii


def fn(c1, c2, c3):
    if 0 == c2:
        return c1[c3:]

    r = c1[0: c2]
    r += c1[c2 + c3:]
    return r


if __name__ == '__main__':
    url = 'https://www.endata.com.cn/API/GetData.ashx'
    data = {
        'year': '2021',
        'MethodName': 'BoxOffice_GetYearInfoData'
    }

    resp = requests.post(url=url, data=data)
    data = resp.text

    a = int(data[len(data) - 1], 16) + 9
    b = int(data[a], 16)

    data = fn(data, a, 1)

    a = data[b: b + 8]
    data = fn(data, b, 8)

    b = a.encode('utf-8')
    a = a.encode('utf-8')
    des = DES.new(b)
    data = binascii.a2b_hex(data)
    result = des.decrypt(data)
    print(result.decode('utf-8'))
