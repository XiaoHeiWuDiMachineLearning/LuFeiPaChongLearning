from multiprocessing import Process
def func():
    print('我是子进程处理的任务！！！')
if __name__ == '__main__':
    print('主进程开始执行!!!')
    # 在主进程创建一个子进程
    p = Process(target=func)
    # 启动子进程:子进程进入就绪状态
    p.start()
    