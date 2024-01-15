# 获取jsonCookies
from selenium import webdriver
import time

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
chrome = webdriver.Chrome(options=option)
chrome.get('https://www.zhihu.com/explore')
print(chrome.get_cookies())
chrome.close()