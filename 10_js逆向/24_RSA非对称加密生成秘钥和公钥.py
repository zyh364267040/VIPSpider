# -*- coding = utf-8 -*-
# @Time: 2021/11/9 下午9:14
from Crypto.PublicKey import RSA


if __name__ == '__main__':
    # 1.生成私钥和公钥
    rsa_key = RSA.generate(2048)

    private_key = rsa_key.exportKey()
    public_key = rsa_key.publickey().exportKey()
    print(private_key, public_key)

    with open('private_key.txt', 'wb') as f:
        f.write(private_key)

    with open('public_key.txt', 'wb') as f:
        f.write(public_key)
