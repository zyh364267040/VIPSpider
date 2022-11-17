# -*- coding = utf-8 -*-
# @Time: 2022/5/26 下午10:15
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def aes_encrypt(data_string):
    key = 'fd6b639dbcff0c2a1b03b389ec763c4b'
    iv = '77b07a672d57d64c'
    aes = AES.new(
        key=key.encode('utf-8'),
        mode=AES.MODE_CBC,
        iv=iv.encode('utf-8')
    )
    raw = pad(data_string.encode('utf-8'), 16)
    return aes.encrypt(raw)


def main():
    data = '1sdfhnajkhgaghjghjhgj'
    result = aes_encrypt(data)
    print(result)


if __name__ == '__main__':
    main()
