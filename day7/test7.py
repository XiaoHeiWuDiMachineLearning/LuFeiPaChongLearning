from threading import Thread
import time
def work():
    global n
    n = 0    # 将全局变量修改为0
if __name__ == '__main__':
    n = 1    # 全局变量
    t = Thread(target=work)
    t.start()
    print(n)