import time
import asyncio

async def get_request(url):
    print('请求', url)
    await asyncio.sleep(2)    # asyncio支持异步的模块
    print('数据请求结束', url)

if __name__ == '__main__':
    start = time.time()
    urls = ['1,com', '2.com', '3.com']
    tasks = []    # 存放创建好的多个任务对象
    for url in urls:
        c = get_request(url)
        task = asyncio.ensure_future(c)
        tasks.append(task)
    # 将tasks列表中存储的3个任务对象，存放到事件循环对象中
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(asyncio.wait(tasks)))
    print('总耗时:', time.time()-start)