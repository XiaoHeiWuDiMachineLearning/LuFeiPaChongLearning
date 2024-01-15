import asyncio
import requests
from lxml import etree
import time
import aiohttp

# 获取网络请求
async def get_request(url):
    page_text = 'null'
    sess = aiohttp.ClientSession()
    response =  await sess.get(url)
    page_text = await response.text()
    return page_text

# 回调函数
def parse(c):
    res = c.result()
    print(res)

if __name__ == '__main__':
    urls = ['https://www.baidu.com/', 'https://www.sougou.com', 'https://www.sina.com']
    start_time = time.time()
    tasks = []
    # 获取任务对象
    for url in urls:
        c = get_request(url)
        task = asyncio.ensure_future(c)
        tasks.append(task)
        task.add_done_callback(parse)
    # 获取事件循环
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print('所用时间:', time.time()-start_time)

