# 爬取豆瓣电影中动态加载电影的详情数据
from time import sleep
from selenium import webdriver
from lxml import etree

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=option)
driver.get('https://movie.douban.com/typerank?type_name=%E6%82%AC%E7%96%91&type=10&interval_id=100:90&action=')
sleep(1)
# 滑动滚轮
driver.execute_script('document.documentElement.scrollTo(0,2000)')
sleep(1)
# 获取页面源码数据
page_text = driver.page_source
# print(page_text)
# 解析电影详情数据
selector = etree.HTML(page_text)
divs = selector.xpath("//div[@class='movie-list-item playable unwatched']")
for div in divs:
    title = div.xpath('.//span[@class="movie-name-text"]/a/text()')[0]
    authors = div.xpath('.//div[@class="movie-crew"]/text()')[0]
    rate = div.xpath('.//span[@class="rating_num"]/text()')[0]
    print(title, '=======>', authors, '==============================>', rate)

