# -*- coding = utf-8 -*-
# @Time: 2021/11/7 下午9:54
from hashlib import md5


if __name__ == '__main__':
    # 加盐
    salt = b'zhouyanhuizhouyanhuizhouyanhuizhouyanhui'
    # 加密器
    obj = md5(salt)

    # 准备好要加密的内容
    password = 'zhou'
    # 设计,是为了应对各种环境
    # 字符串可以进行md5运算
    # 对某个文件进行计算md5的值
    obj.update(password.encode('utf-8'))

    # 获取密文
    md5_miwen = obj.hexdigest()
    print(md5_miwen)
