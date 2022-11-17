# -*- coding = utf-8 -*-
# @Time: 2022/5/26 下午10:32
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii


KEY = "4E2918885FD98109869D14E0231A0BF4"
KEY = binascii.a2b_hex(KEY)

IV = "16B17E519DDD0CE5B79D7A63A4DD801C"
IV = binascii.a2b_hex(IV)


def aes_encrypt (data_string) :
    aes = AES.new(
        key=KEY,
        mode=AES.MODE_CBC,
        iv=IV
    )

    raw = pad (data_string.encode ('utf-8'), 16)
    aes_bytes = aes.encrypt(raw)

    return binascii.b2a_hex(aes_bytes).decode().upper()
data = "|878975262|d000035rirv|1631615607|mg3c3b04ba|1.3.5|ktjwlm89_to920weqpg|4330701|https://w.yangshipin.cn/|mozilla/5.0 (macintosh; ||Mozilla|Netscape|MacIntel|"
result = aes_encrypt (data)
print(result)
