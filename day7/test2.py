from multiprocessing import Process

def func(num1, num2):
    print('我是一个绑定给子进程的一组任务！！！', num1, num2)

if __name__ == '__main__':
    print('主进程开始执行!!')
    # 创建一个进程p,给该进程绑定一组任务
    p = Process(target=func, args=(123, 456))
    # 启动创建好的进程
    p.start()
    print('主进程执行完毕！！')