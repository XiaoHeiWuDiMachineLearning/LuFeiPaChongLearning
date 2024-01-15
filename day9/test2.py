
chromedriver_path = r"D:\Anaconda\envs\xizhi\Lib\webdriver\chromedriver.exe"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
# 创建/打开指定的浏览器
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=option)
# 发起网络请求
driver.get("https://www.jd.com/")
# 输入搜索内容
search_text = driver.find_element(By.XPATH,'//*[@id="key"]')
search_text.send_keys('能量胶')
sleep(1)
# 点击搜索框
btn = driver.find_element(By.XPATH, '//*[@id="search"]/div/div[2]/button')
btn.click()

