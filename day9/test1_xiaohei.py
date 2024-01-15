import requests
import re
from tqdm import tqdm
import asyncio
import aiohttp

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}
# 协程函数
async def parse(dict_):
    async with aiohttp.ClientSession() as sess:
        async with await sess.get(url=dict_['url'], headers=headers) as response:
            content = await response.read()
            dict_['content'] = content
    return dict_
# 回调函数
def call_back(t):
    dict_ = t.result()
    with open(dict_['path'], 'wb') as f:
        f.write(dict_['content'])
    print(dict_['title'], '已写入........')
if __name__ == '__main__':
    tasks = []
    m1_url = 'https://v4.dious.cc/20220519/MIIwfI7B/index.m3u8'

    m1_text = requests.get(url=m1_url, headers=headers).text
    '''
    #EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1200000,RESOLUTION=1280x720
    /20220519/MIIwfI7B/1200kb/hls/index.m3u8#EXTM3U
    '''
    # 获取m2_url
    m2_url = 'https://v4.dious.cc'+m1_text.strip().split('\n')[-1]
    # 获取二级m3u8文件内容
    m2_text = requests.get(url=m2_url, headers=headers).text
    pattern = '.*\.ts'
    ts_s = re.findall(pattern, m2_text)
    # 存放路径
    dir_ = './m3u8_vedio/'
    for ts_path in ts_s:
        # 获取文件名
        title = ts_path.strip().split('/')[-1]
        # 获取下载url
        ts_url = 'https://v4.dious.cc/'+ts_path
        # 任务字典
        dict_ = {'title': title, 'url': ts_url, 'path': dir_ + title}
        task = asyncio.ensure_future(parse(dict_))
        task.add_done_callback(call_back)
        tasks.append(task)
    # 获取事件循环
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))