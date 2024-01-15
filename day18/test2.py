from Crypto.PublicKey import RSA


# 构建RSA算法对象
rsakey = RSA.generate(1024)
# 生成公钥
# print('公钥:', rsakey.public_key().exportKey())
with open('rsa.public.pem', 'wb') as f:
    f.write(rsakey.public_key().exportKey())
# 生成私钥
with open('rsa.private.pem', 'wb') as f:
    f.write(rsakey.exportKey())
# print('私钥:', rsakey.exportKey())