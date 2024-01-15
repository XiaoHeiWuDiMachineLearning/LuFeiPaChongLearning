# 加锁前代码
# {'count':1}
from multiprocessing import Process
import time
import json
import random
from multiprocessing import Lock


def search():    # 查询db文件中的余票数量
    fp = open('./db.json', 'r')
    dic = json.load(fp)    # 反序列化
    print('剩余车票数量为:', dic['count'])

def get():  # 负责检票

    fp = open('./db.json', 'r')
    dic = json.load(fp)
    time.sleep(0.1)
    if dic['count'] > 0:
        time.sleep(0.2)
        dic['count'] -= 1
        time.sleep(0.1)
        # 存储
        json.dump(dic, open('./db.json', 'w'))
        print('购票成功')


def task(lock):
    lock.acquire()
    search()
    get()
    lock.release()
if __name__ == '__main__':
    lock = Lock()
    for i in range(3):
        p = Process(target=task, args=(lock, ))
        p.start()