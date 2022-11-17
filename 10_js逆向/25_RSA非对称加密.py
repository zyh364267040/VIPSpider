# -*- coding = utf-8 -*-
# @Time: 2021/11/12 下午6:46
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import base64


if __name__ == '__main__':
    # 1.明文
    massage = '这是我要加密的内容'
    # 2.读取公钥
    with open('public_key.txt', 'r', encoding='utf-8') as f:
        # 3.把公钥字符串转化成rsa_key
        rsa_key = RSA.importKey(f.read())
    # 4.创建加密对象
    rsa = PKCS1_v1_5.new(rsa_key)
    # 5.加密
    miwen = rsa.encrypt(massage.encode('utf-8'))
    # 6.b64处理
    miwen = base64.b64encode(miwen).decode('utf-8')
    print(miwen)
