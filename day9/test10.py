# 获取jsonCookies
from selenium import webdriver
import time

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
chrome = webdriver.Chrome(options=option)
chrome.get('https://www.zhihu.com/explore')
cookies = chrome.get_cookies()
# 解析cookies
dic = {}
for cookie in cookies:
    key = cookie['name']
    value = cookie['value']
    dic[key] = value
print(dic)
chrome.close()