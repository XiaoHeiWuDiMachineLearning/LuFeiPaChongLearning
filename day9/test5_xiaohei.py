from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from lxml import etree
import requests
import cv2
import base64
import json
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

def get_distance():
    background = cv2.imread("background.png", 0)
    gap = cv2.imread("gap.png", 0)

    res = cv2.matchTemplate(background, gap, cv2.TM_CCOEFF_NORMED)
    value = cv2.minMaxLoc(res)[2][0]
    print(value)
    return value * 278 / 360

def base64_api(uname='111123', pwd='xiaohei', img='background.png', typeid=33):
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
    # 浏览器基础配置
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver=webdriver.Chrome(options=option)
    # Selenium在打开任何页面之前，先运行这个Js文件。
    with open('./stealth.min.js') as f:
        js = f.read()
    # 进行js注入，绕过检测
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })

    # 发送请求
    driver.get('https://www.jd.com')


    # 点击登录进入登录界面
    login_ = driver.find_element(By.XPATH, '//li[@id="ttbar-login"]/a')
    login_.click()


    # 输入用户名密码
    sleep(2)
    driver.find_element(By.XPATH, '//input[@id="loginname"]').send_keys('1820161379')
    sleep(1)
    driver.find_element(By.XPATH, '//input[@id="nloginpwd"]').send_keys('BwuAdmin123')

    # 点击登录按钮
    driver.find_element(By.XPATH, '//a[@id="loginsubmit"]').click()
    while True:
        print('开始下载滑块图片')
        # 图片的xpath路径
        sleep(2)
        background_xpath = "//div[@class='JDJRV-bigimg']/img"
        gap_xpath = "//div[@class='JDJRV-smallimg']/img"
        # 通过xpath下载图片
        ground_img64_code = driver.find_element(By.XPATH, background_xpath).get_attribute('src')
        ground_img64_code = ground_img64_code.split(',')[1]
        ground_img_code = base64.b64decode(ground_img64_code)
        gap_img64_code  = driver.find_element(By.XPATH, gap_xpath).get_attribute('src')
        gap_img64_code = gap_img64_code.split(',')[1]
        gap_img_code = base64.b64decode(gap_img64_code)
        with open('background.png', 'wb') as f:
            f.write(ground_img_code)
        with open('gap.png', 'wb') as f:
            f.write(gap_img_code)
        print('图片下载完毕')


        # 计算距离并移动
        gapDiv_xpath = '//div[@class="JDJRV-slide-inner JDJRV-slide-btn"]'
        print('滑块下载成功,正在调用cv2计算滑块所需滑动距离')
        dis = get_distance()
        # dis = int(base64_api()) * 278.0 / 360
        gap_div = driver.find_element(By.XPATH, gapDiv_xpath)
        print('开始拖拽元素.....')
        sleep(1)
        action = ActionChains(driver)
        action.click_and_hold(gap_div).perform()    # 长按
        action.move_by_offset(dis, 0).perform()  # 拖拽
        action.release(on_element=gap_div).perform()     # 释放
        sleep(5)