from lxml import etree
import requests
import aiohttp
import time
from tqdm import tqdm
import os
import asyncio


# 存放图片链接信息
items = []
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

async def parse(dict_):
    async with aiohttp.ClientSession() as sess:
        async with await sess.get(url=dict_['url'], headers=headers) as response:
            img_content = await response.read()
            dict_['img_content'] = img_content
    return dict_

def backup(t):
    dict_ = t.result()
    with open(dict_['path'], 'wb') as f:
        f.write(dict_['img_content'])
        print(dict_['path'], '已写入.....')

if __name__ == '__main__':
    dirName = 'imgLibs'


    start_time = time.time()
    if not os.path.exists(dirName):
        os.mkdir(dirName)
    # 请求前n个页面
    url = 'https://www.pkdoutu.com/article/list/?page=%d'
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
            dict_ = {}
            img_src = img_src[0]
            img_title = img_src.split('/')[-1]
            img_path = dirName + '/' + img_title
            dict_['url'] = img_src
            dict_['path'] = img_path
            items.append(dict_)

    # 构建协程对象
    tasks = []
    for dict_ in items:
        t = parse(dict_)
        task = asyncio.ensure_future(t)
        task.add_done_callback(backup)
        tasks.append(task)
    # 获取事件循环
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print('总耗时:', time.time()-start_time)