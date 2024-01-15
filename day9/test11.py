# https://www.17k.com/
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import os
import json
import requests
from lxml import etree
# accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F06%252F66%252F99%252F100829966.jpg-88x88%253Fv%253D1690875618000%26id%3D100829966%26nickname%3D%25E5%25B0%258F%25E9%25BB%2591%25E6%2597%25A0%25E6%2595%258C%25E9%2585%2592%25E9%2587%258F%26e%3D1713599838%26s%3Da3bb14ed41f1e882;
url = 'https://www.17k.com/'
if not os.path.exists('book_cookie.json'):
    # 获取浏览器选项
    option = webdriver.ChromeOptions()
    option.add_experimental_option('detach', True)
    # 生成浏览器selenium对象
    chrome = webdriver.Chrome(options=option)
    chrome.get(url)
    # 登录对话框按钮
    login_xpath = """//a[@href="javascript:k.login('login')"]"""
    chrome.find_element(By.XPATH, login_xpath).click()
    sleep(2)
    # 切换到对应frame
    frame_xpath = '//div[@class="QUI_POP_CONT"]/iframe'
    frame = chrome.find_element(By.XPATH, frame_xpath)
    chrome.switch_to.frame(frame)
    # 输入用户名密码
    user_xpath = '//input[@name="user"]'
    pass_xpath = '//input[@name="pass"]'
    select_xpath = '//input[@id="protocol"]'
    chrome.find_element(By.XPATH, user_xpath).send_keys('18201611379')
    sleep(1)
    chrome.find_element(By.XPATH, pass_xpath).send_keys('BwuAdmin123')
    sleep(2)
    # 点击同意协议
    chrome.find_element(By.XPATH, select_xpath).click()
    sleep(1)
    # 登录提交
    submit_xpath = '//input[@type="submit"]'
    chrome.find_element(By.XPATH, submit_xpath).click()
    sleep(4)
    # 获取cookie
    cookies = chrome.get_cookies()
    # 解析cookies
    dic = {}
    for cookie in cookies:
        key = cookie['name']
        value = cookie['value']
        dic[key] = value
    with open('book_cookie.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(dic))
    chrome.close()
# 使用cookies发起请求
url = 'https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919'
cookies = {}
with open('book_cookie.json', 'r', encoding='utf-8') as f:
    cookies = json.loads(f.read(), strict=False)
print(cookies)
# headers['cookie'] = cookies
response = requests.get(url, cookies=cookies)
response.encoding = 'utf-8'

print(response.text)
# print(response.text)