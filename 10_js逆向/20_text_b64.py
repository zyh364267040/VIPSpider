# -*- coding = utf-8 -*-
# @Time: 2021/11/7 下午10:40
import base64


if __name__ == '__main__':
    s = '我饿了,要吃饭'.encode('utf-8')
    b64 = base64.b64encode(s)
    b64_str = b64.decode('utf-8')
    print('b64编码后:', b64_str)

    b64 = b64_str.encode('utf-8')
    s = base64.b64decode(b64)
    print(s.decode('utf-8'))
