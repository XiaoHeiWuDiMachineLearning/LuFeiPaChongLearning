from threading import Thread, Lock
import time
import random

def work():
    global n
    lock.acquire()
    temp = n
    time.sleep(random.random())
    n = temp - 1
    lock.release()

if __name__ == '__main__':
    n = 10    # 全局变量
    ts = []
    lock = Lock()
    for i in range(10):
        t = Thread(target=work)
        t.start()
        ts.append(t)
    for t in ts:
        t.join()
    print('全局变量n的值为:', n)