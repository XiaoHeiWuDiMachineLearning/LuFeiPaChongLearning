# ASCII编码 GBK unicode utf8(针对ASCII一个字节,针对汉字三个字节)
from urllib import parse

# 值编码
value = parse.quote('&&222==333')
print(value)
# 键值编码
data = {'wd':'&&7www', 'name':'小黑'}
print(parse.urlencode(data))