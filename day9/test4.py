from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
# 浏览器基础配置
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=option)
# 发送请求
driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
sleep(2)
# 定位标签
driver.switch_to.frame('iframeResult')
div = driver.find_element(By.XPATH, '//*[@id="draggable"]')
# 长按
action = ActionChains(driver)
action.click_and_hold(div).perform()
action.move_by_offset(100, 100).perform()