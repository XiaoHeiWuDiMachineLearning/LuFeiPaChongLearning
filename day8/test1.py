import asyncio
'''
函数在函数定义前加上一个async关键字。特殊之处:
    1.被调用后返回一个协程对象。
    2.函数调用后函数内部的程序语句不会被立即执行。
    3.
任务对象
事件循环
'''
async def func():
    print('I am xiaohei')
    return 123

def haha(c):    # 给任务对象绑定的回调函数，必须要有一个参数
    # 参数表示回调函数的绑定者（任务对象）
    print('我是任务对象的回调,result返回的是:', c.result())
    # 返回的是特殊函数内部返回值
c = func()
# 特殊函数==指定形式的操作==协程
# 创建一个任务对象
task = asyncio.ensure_future(c)
# 可以给任务对象绑定一个回调函数:回头调用的函数
task.add_done_callback(haha)
# 任务对象==高级的协程==一组指定形式的操作
# 如何执行任务？通过事件循环对象
loop = asyncio.get_event_loop()
# 将任务对象存储到loop，并且启动loop
loop.run_until_complete(task)