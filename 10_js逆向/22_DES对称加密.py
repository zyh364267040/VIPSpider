# -*- coding = utf-8 -*-
# @Time: 2021/11/9 下午5:05
from Crypto.Cipher import DES


if __name__ == '__main__':
    s = '我爱黎明'

    des = DES.new(b'zhouzhou', mode=DES.MODE_CBC, IV='01020304')
    bs = s.encode('utf-8')
    que = 8 - len(bs) % 8
    bs += (que * chr(que)).encode('utf-8')
    result = des.encrypt(bs)
    print(result)

    miwen = b'n\x0c2\x15\xcd\xb3W\x92k\xf2\x8aHP:\xa2\x9b'
    des = DES.new(b'zhouzhou', mode=DES.MODE_CBC, IV='01020304')
    result = des.decrypt(miwen)
    print(result.decode('utf-8'))
