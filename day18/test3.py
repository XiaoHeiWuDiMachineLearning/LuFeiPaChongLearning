import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

b64encode_encrypt_data = 'aa1XFIhVbz+6NNHOZcZFlA=='
# 进行base64解码
encrypt_data = base64.b64decode(b64encode_encrypt_data)
print('encrypt_data:', encrypt_data)
# aes解密
key = '0123456789abcdef'.encode()
iv = '0123456789abcdef'.encode()
aes = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
data = aes.decrypt(encrypt_data)
print('源数据:', unpad(data, 16).decode())