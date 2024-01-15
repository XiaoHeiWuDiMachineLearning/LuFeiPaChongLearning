from lxml import etree
import requests
import aiohttp
import time
from tqdm import tqdm

# 需求:将1-10页对应的图片数据进行爬取
# 模式分析:
    #1.需要请求多少次:10 500
    # 异步操作不是作用在爬虫的所有环节，而是在耗时的环节
    # 使用requests请求10页的页面源码数据，使用aiohttp异步操作请求所有的图片数据
if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    }
    url = 'https://www.pkdoutu.com/article/list/?page=%d'
    image_urls = []
    # 请求前n页的页码数据
    for i in range(1, 6):
        response = requests.get(url%i, headers=headers)
        s = etree.HTML(response.text)
        xpath = '//a[@class="list-group-item random_list"]//img/@data-original'
        srcs = s.xpath(xpath)
        image_urls.extend(srcs)
    # 开始解析图片
    print('开始解析图片')
    for image_url in tqdm(image_urls):
        content = requests.get(image_url, headers=headers).content
        title = image_url.split('/')[-1]
        with open('./doutu/'+title, 'wb') as f:
            f.write(content)
