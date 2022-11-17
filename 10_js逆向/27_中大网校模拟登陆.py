# -*- coding = utf-8 -*-
# @Time: 2021/11/13 下午3:44
import requests
import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64


# 获取session,用于携带cookies
session = requests.session()

# 加密的公钥
public_key = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDA5Zq6ZdH/RMSvC8WKhp5gj6Ue4Lqjo0Q2PnyGbSkTlYku0HtVzbh3S9F9oHbxeO55E8tEEQ5wj/+52VMLavcuwkDypG66N6c1z0Fo2HgxV3e0tqt1wyNtmbwg7ruIYmFM+dErIpTiLRDvOy+0vgPcBVDfSUHwUSgUtIkyC47UNQIDAQAB'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Referer': 'https://user.wangxiao.cn/login',
    'Content-Type': 'application/json;charset=UTF-8'
}


# 发送请求,获取响应
def send_request(method, url, data=None):
    # 发送请求,获取响应
    if method == 'get':
        res = session.get(url, headers=headers, data=data)
    else:
        res = session.post(url, headers=headers, data=data)

    # 返回响应
    return res


# 图鉴打码平台识别验证码
def base64_api(img):
    data = {"username": 'q6035945', "password": 'q6035945', "typeid": 1003, "image": img}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]


# RSA加密
def rsa_encrypt(password):
    # 把公钥转换成rsa_key
    rsa_key = RSA.importKey(base64.b64decode(public_key))
    # 创建加密对象
    rsa = PKCS1_v1_5.new(rsa_key)
    # 加密
    miwen = rsa.encrypt(password.encode('utf-8'))
    # 使用b64处理密文
    miwen = base64.b64encode(miwen).decode('utf-8')

    # 将密文返回
    return miwen


def run():
    # 用户名
    username = '18614075987'
    # 密码
    password = 'q6035945'
    # 1.进入到登录页面 -> 加载到cookie
    # 登录页url,用于获取cookies
    url = 'https://user.wangxiao.cn/login'
    # 发送请求,获取携带cookies的session,以及sessionId
    res = send_request('get', url)
    session_id = res.cookies.get('sessionId')

    # 2.获取到验证码 -> 打码平台,搞定验证码
    # 验证码url
    verify_code_url = 'https://user.wangxiao.cn/apis//common/getImageCaptcha'
    # 发送请求,获取验证码的响应
    verify_code_url_res = send_request('post', verify_code_url)
    # 获取验证码b64字符串
    verify_code_b64 = verify_code_url_res.json()['data'].split(',')[-1]
    # 获取验证码
    verify_code = base64_api(verify_code_b64)

    # 3.把密码进行加密
    # 获取与密码共同加密的数据url
    get_time_url = 'https://user.wangxiao.cn/apis//common/getTime'
    # 获取与密码共同加密的数据
    res = send_request('post', get_time_url)
    time_data = res.json()['data']
    # 拼接需加密的密码和时间数据
    password = password + time_data
    miwen = rsa_encrypt(password)

    # 4.进行登录
    # 登录所需data数据
    data = {
        'imageCaptchaCode': verify_code,
        'password': miwen,
        'userName': username
    }
    # 登录的url
    login_url = 'https://user.wangxiao.cn/apis//login/passwordLogin'
    # 发送登陆请求,获取登录后的响应数据
    login_res = send_request('post', login_url, data=json.dumps(data))
    login_info = login_res.json()['data']

    # 5.对登录后的cookie信息进行整理
    cookies_doc = {
        "autoLogin": "null",
        "OldPassword": login_info['passwordCookies'],
        "OldPassword_": login_info['passwordCookies'],
        "OldUsername": login_info['userNameCookies'],
        "OldUsername_": login_info['userNameCookies'],
        "OldUsername2": login_info['userNameCookies'],
        "OldUsername2_": login_info['userNameCookies'],
        f"{login_info['userName']}_exam": login_info['sign'],
        "token": login_info['token'],
        "UserCookieName": login_info['userName'],
        "UserCookieName_": login_info['userName'],
        "userInfo": login_info,
        "sessionId": session_id
    }
    print(cookies_doc)


if __name__ == '__main__':
    run()
