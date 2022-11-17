# -*- coding = utf-8 -*-
# @Time: 2021/11/7 下午10:19
from urllib.parse import urlencode, unquote


if __name__ == '__main__':
    # url的编码
    url = 'https://www.baidu.com/s?'
    parm = {
        'wd': '我饿了'
    }

    result = urlencode(parm)
    print(result)

    # 把编码的内容转换回来
    result = unquote(url+result)
    print(result)
