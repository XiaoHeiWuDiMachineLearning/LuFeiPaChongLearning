from lxml import etree
import requests
import aiohttp
import time
from tqdm import tqdm
import os
import asyncio
# 同步:67s
# 需求:将1-10页对应的图片数据进行爬取
# 模式分析:
    #1.需要请求多少次:10 500
    # 异步操作不是作用在爬虫的所有环节，而是在耗时的环节
    # 使用requests请求10页的页面源码数据，使用aiohttp异步操作请求所有的图片数据

async def get_request(dic):
    async with aiohttp.ClientSession() as sess:
        async with await sess.get(url=dic['img_src'], headers=headers) as response:
            img_data = await response.read()
            dic['img_data'] = img_data
    return dic

def saveImg(t):
    dic = t.result()
    img_path = dirName + '/' + dic['img_title']
    with open(img_path, 'wb') as fp:
        fp.write(dic['img_data'])
        print(dic['img_title'], '被下载保存成功')
if __name__ == '__main__':
    dirName = 'imgLibs'
    start_time = time.time()
    if not os.path.exists(dirName):
        os.mkdir(dirName)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    }
    # 请求前n个页面
    url = 'https://www.pkdoutu.com/article/list/?page=%d'
    # 存储图片相关信息
    img_msg = []
    for page in range(1, 6):
        new_url = url%page    # 每一个页码对应的页面url
        page_text = requests.get(new_url, headers=headers).text
        # 数据解析每一个图片链接
        tree = etree.HTML(page_text)
        a_list = tree.xpath('//a[@class="list-group-item random_list"]//img')
        for a in a_list:
            img_src = a.xpath('./@data-original')
            if not img_src:
                continue
            img_src = img_src[0]
            img_title = img_src.split('/')[-1]
            dic = {}
            dic['img_src'] = img_src
            dic['img_title'] = img_title
            img_msg.append(dic)
    tasks = []
    for dic in img_msg:
        c = get_request(dic)
        task = asyncio.ensure_future(c)
        task.add_done_callback(saveImg)
        tasks.append(task)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print('总耗时:', time.time()-start_time)

