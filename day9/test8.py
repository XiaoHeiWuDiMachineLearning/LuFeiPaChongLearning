import base64
import json
import requests


# 一、图片文字类型(默认 3 数英混合)：
# 1 : 纯数字
# 1001：纯数字2
# 2 : 纯英文
# 1002：纯英文2
# 3 : 数英混合
# 1003：数英混合2
#  4 : 闪动GIF
# 7 : 无感学习(独家)
# 11 : 计算题
# 1005:  快速计算题
# 16 : 汉字
# 32 : 通用文字识别(证件、单据)
# 66:  问答题
# 49 :recaptcha图片识别
# 二、图片旋转角度类型：
# 29 :  旋转类型
#
# 三、图片坐标点选类型：
# 19 :  1个坐标
# 20 :  3个坐标
# 21 :  3 ~ 5个坐标
# 22 :  5 ~ 8个坐标
# 27 :  1 ~ 4个坐标
# 48 : 轨迹类型
#
# 四、缺口识别
# 18 : 缺口识别（需要2张图 一张目标图一张缺口图）
# 33 : 单缺口识别（返回X轴坐标 只需要1张图）
# 五、拼图识别
# 53：拼图识别
# 函数实现忽略
def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""


def getImgCodeText(imgPath, imgType):  # 直接返回验证码内容
    # imgPath：验证码图片地址
    # imgType：验证码图片类型
    result = base64_api(uname='图鉴的账号', pwd='图鉴的密码', img=imgPath, typeid=imgType)
    return result




from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
import tujian

# 1.创建浏览器对象
bro = webdriver.Chrome(executable_path='../chromedriver')
# 2.发起请求
login_url = 'https://passport.bilibili.com/login?from_spm_id=333.851.top_bar.login_window'
bro.get(login_url)
sleep(1)
# 3.定位到指定标签填充用户名和密码
user_box = bro.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/input')
user_box.send_keys('15027900535')
sleep(1)
pwd_box = bro.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[1]/div[3]/input')
pwd_box.send_keys('123456')
sleep(1)
login_btn = bro.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]')
login_btn.click()
sleep(10)
# 4.定位完整的验证码对话框
# 注意：在开发者工具中是可以定位到多个div表示验证码对话框的，因此将这几个div都定位到，以此去尝试
code_tag = bro.find_element_by_xpath('/html/body/div[4]/div[2]/div[6]/div/div')
sleep(1)
# 5.识别验证码（使用打码平台进行验证码识别）
code_tag.screenshot('./code.png')  # 将验证码对话框截图保存
sleep(1)
# 使用图鉴接口识别
result = tujian.getImgCodeText('./code.png', 27)  # 获取了识别的结果
# result = '154,251|145,167'
# print(result)
result_list = result.split('|')
# result_list == ['154,251','145,167']
# 6.根据识别出验证码的结果进行处理
for pos in result_list:
    x = int(pos.split(',')[0])
    y = int(pos.split(',')[1])
    ActionChains(bro).move_to_element_with_offset(code_tag, x, y).click().perform()
    sleep(0.5)
sleep(2)
# 此处使用class属性进行确定标签定位
confirm_btn = bro.find_element_by_xpath('//a[@class="geetest_commit"]')
confirm_btn.click()
sleep(3)
bro.quit()