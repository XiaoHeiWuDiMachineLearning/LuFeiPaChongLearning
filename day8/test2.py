import asyncio
import time

async def get_request(url):
    print('正在请求%s数据....'%url)
    time.sleep(2)
    print('数据请求结束%s'%url)

if __name__ == '__main__':
    # 创建一个协程对象
    c = get_request('www.1.com')
    # 创建任务对象
    task = asyncio.ensure_future(c)
    # 创建事件循环对象
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task)

