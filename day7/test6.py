from threading import Thread
import time

def func(num):
    time.sleep(1)
    print("num的值为:", num)

if __name__ == '__main__':
    start = time.time()
    t_list = []
    for i in range(3):
        # 创建好了一个子线程
        t = Thread(target=func, args=(1, ))
        t_list.append(t)
        t.start()
    for t in t_list:
        t.join()
    print('总耗时:', time.time()-start)
