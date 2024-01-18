import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import json
url = 'http://127.0.0.1:5000/books'
# 进行base64编码
for i in range(1, 6):
    param = {"page":str(i)}
    # json.dumps一定要去除空格
    s = json.dumps(param, separators=(',', ':'))
    # 填充，以便准备进行AES.CBC加密算法
    s = pad(s.encode(), block_size=16)
    #print(s)
    # 进行AES加密
    key = '0123456789abcdef'
    iv = '0123456789abcdef'
    # 构造AES对象
    aes = AES.new(key=key.encode(), iv=iv.encode(), mode=AES.MODE_CBC)
    s = aes.encrypt(s)
    #print(s)
    encrypt_data = base64.b64encode(s)
    # 构造请求参数
    param['sign'] = encrypt_data.decode()
    # 发送请求
    response = requests.get(url=url, params=param)
    print(response.json())
# "KjdefP9ReA6Qn+sqiGGgqQ=="