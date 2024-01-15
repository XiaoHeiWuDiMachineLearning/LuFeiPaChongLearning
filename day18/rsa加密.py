from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64


data = 'alex is a monkey!'

# rsa: 公钥加密私钥解密,用于数据加密
# rsa: 私钥加密公钥解密,用于数字签名

with open('rsa.public.pem', 'r') as f:
    pk = f.read()
    # 获取公钥对象
    rsa_pk = RSA.importKey(pk)
    # 获取rsa算法对象
    rsa = PKCS1_v1_5.new(rsa_pk)
    # 基于rsa进行加解密
    encrypt_data = rsa.encrypt(data.encode())
    print('encrypt_data:', encrypt_data)
    # 为了在网络中正确传输，进行一个base64封装
    base64_encrypt_data = base64.b64encode(encrypt_data)
    print('base64编码:', base64_encrypt_data.decode())
