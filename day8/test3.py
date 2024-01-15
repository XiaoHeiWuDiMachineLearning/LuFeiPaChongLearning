import asyncio
import time


async def get_request(url):
    print('正在请求%s数据....'%url)
    # 不支持异步
    time.sleep(2)
    print('数据请求结束%s'%url)

if __name__ == '__main__':
    start_time = time.time()
    urls = ['1', '2', '4']
    tasks = []
    for url in urls:
        c = get_request(url)
        task = asyncio.ensure_future(c)
        tasks.append(task)
    loop = asyncio.get_event_loop()
    # 挂起：让被挂起的任务对象交出cpu的使用权
    loop.run_until_complete(asyncio.wait(tasks))
    # 在特殊函数内部，不可以出现不支持异步的操作代码
    print('总耗时:', time.time()-start_time)