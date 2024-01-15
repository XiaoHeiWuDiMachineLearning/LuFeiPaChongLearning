from multiprocessing import Process
import time

ticketNum = 10
class A:
    t = 1

def func(num, a):
    print('我是一个子进程，我要购买%d张票！'%num)
    global ticketNum
    ticketNum -= num
    a.t += 1
    time.sleep(2)

if __name__ == '__main__':
    ticketNum = 10    # 全部的车票
    a = A()
    p = Process(target=func, args=(3, a))
    # p.daemon = True
    p.start()
    # 主进程在子进程结束之后再结束

    p.join()
    print('目前剩余车票数量为:', ticketNum)
    print(a.t)
    # 进程与进程之间是完全独立。两个进程对应的是两块独立的内存空间，每一个进程只可以访问