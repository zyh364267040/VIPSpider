# -*- coding = utf-8 -*-
# @Time: 2021/11/8 下午9:48
from Crypto.Cipher import AES
import base64


if __name__ == '__main__':
    s = '这是我要加密的明文'

    aes = AES.new(b'zhouyanhui111111', mode=AES.MODE_CBC, IV=b'0102030405060708')

    # 需要做填充,填充最好的方案(通用:缺少字节的个数 * chr(缺少字节的个数)
    bs = s.encode('utf-8')

    # 缺少字节个数
    que = 16 - len(bs) % 16
    bs += (que * chr(que)).encode('utf-8')

    # 需求加密的内容必须是字节
    result = aes.encrypt(bs)
    print(result)

    b64 = base64.b64encode(result).decode()
    print(b64)

    # 如果aes对象经过了加密,就不能在解密了,必须重新写
    miwen = '8qBgfHnOlABbU0xOaOebyuCWF7yxNZoK0aOHxbsnZm8='
    aes = AES.new(b'zhouyanhui111111', mode=AES.MODE_CBC, IV=b'0102030405060708')
    # 处理base64
    bs = base64.b64decode(miwen)
    result = aes.decrypt(bs)
    print(result.decode('utf-8').strip(""))
