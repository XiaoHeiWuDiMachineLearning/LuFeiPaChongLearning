# 爬虫多任务处理示范(默写)
import asyncio
import requests
from lxml import etree
import time
import aiohttp


urls = ['https://www.baidu.com/', 'https://www.sougou.com', 'https://www.sina.com']

# 实现网络请求获取源码数据
async def get_request(url):
    # requests是不支持异步的
    # response = requests.get(url)
    # aiohttp是一种支持异步的网络请求模块
    # page_text = response.text
    # return page_text
    # 创建了一个请求对象
    async with aiohttp.ClientSession() as sess:    # sess = aiohttp.ClientSession()
        # 使用请求对象进行请求发送
        async with await sess.get(url=url) as response:
            # 获取字符串形式响应数据
            page_text = await response.text()
            # response.read()获取二进制形式的响应数据
    return page_text

# 回调函数:数据解析
def parse(t):
    # 获取任务执行后，拿到的页面源码数据
    page_text = t.result()    # 获取了特殊函数返回值
    # 对页面源码数据进行数据解析
    print(page_text)


if __name__ == '__main__':
    start = time.time()
    tasks = []
    for url in urls:
        c = get_request(url)
        task = asyncio.ensure_future(c)
        task.add_done_callback(parse)
        tasks.append(task)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print('所用时间:', time.time()-start)