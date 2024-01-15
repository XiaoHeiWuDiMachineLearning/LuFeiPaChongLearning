from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from urllib import request
import base64
import requests
import json

def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        #！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
        return result["message"]
    return ""

if __name__ == '__main__':
    # 浏览器配置
    option = webdriver.ChromeOptions()
    option.add_experimental_option('detach', True)
    chrome = webdriver.Chrome(options=option)
    chrome.implicitly_wait(5)
    # 发起请求
    chrome.get('https://www.bilibili.com/')
    sleep(3)
    # 点击登录按钮
    chrome.find_element(By.XPATH, '//*[@id="i_cecream"]/div[2]/div[1]/div[1]/ul[2]/li[1]/li/div[2]/div/div/div[2]').click()
    sleep(5)
    # 输入用户名密码
    username_input = chrome.find_element(By.XPATH, '//div[@class="form__item"]/input[@type="text"]')
    password_input = chrome.find_element(By.XPATH, '//div[@class="form__item"]/input[@type="password"]')
    username_input.send_keys('18201611379')
    password_input.send_keys('xiaoheidiyi123')
    sleep(2)
    chrome.find_element(By.XPATH, '//div[@class="btn_primary "]').click()
    sleep(2)
    # 获取验证码图片
    img = chrome.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[6]/div/div')
    img.screenshot('./img.png')
    print('图片保存成功，准备识别图片坐标位置')
    sleep(2)
    result = base64_api(uname='111123', pwd='xiaohei', img='./img.png', typeid=27)
    print('识别坐标:', result)
    pos = []
    for p in result.strip().split('|'):
        x, y = p.split(',')
        x = int(x)
        y = int(y)
        print(f'点击坐标{x, y}')

        ActionChains(chrome).move_to_element_with_offset(img, x, y).click().perform()

        sleep(0.5)

    chrome.find_element(By.XPATH, '//a[@class="geetest_commit"]').click()
    print('模拟登陆成功，小黑是最棒的！！！干就完了，奥利给！！！！！')