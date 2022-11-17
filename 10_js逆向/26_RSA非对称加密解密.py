# -*- coding = utf-8 -*-
# @Time: 2021/11/12 下午7:09
from Crypto.PublicKey import RSA
import base64
from Crypto.Cipher import PKCS1_v1_5


if __name__ == '__main__':
    # 1.密文
    miwen = 'RJQPs2KDpxU1oVRgVLLj5fDEcoXd2MiEz5dRlZv/fSvmIb4umO+WZLW3cWgcvaRoF5r7QSoRAHhLPZu9HnS3iEu2hdsqrL6olQZfmR7+r34/M4xcXv2AJPjsiGpwOWTTrgBJMdv0OjZFLR2QcsKfPR0Mg0TIi/NMcFCYuCvQqjQ7Nf4oLSnZUw9uzf+wffzcmfH46+DMjALqnWD8y8Ym6WzNo/NbBrr7RR71/irzECS7RMsdD2CY4K3cJwo/NvoekNZadc+AH7HU9boMghQ2is2uZC3KuLMzgu+k28IUb1Gzx+7b2liiWUk7EG0jMonJm6NGUWMhIUctqAAGV/BZRA=='
    # 2.读取秘钥
    with open('private_key.txt', 'r', encoding='utf-8') as f:
        # 3.生成私钥对象
        rsa_key = RSA.importKey(f.read())
    # 4.b64转换
    miwen = base64.b64decode(miwen)
    # 5.生成解密对象
    rsa = PKCS1_v1_5.new(rsa_key)
    # 6.解密
    mingwen = rsa.decrypt(miwen, None)
    print(mingwen.decode('utf-8'))
