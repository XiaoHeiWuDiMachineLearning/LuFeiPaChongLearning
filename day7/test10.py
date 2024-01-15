import time
from threading import Thread
from multiprocessing.dummy import Pool
start = time.time()
pool = Pool()
def get_requests(url):
    print('正在爬取数据', url)
    time.sleep(2)
    print('数据爬取结束', url)

urls = ['www.1.com','www.2.com','www.3.com','www.4.com','www.5.com']
pool.map(get_requests, urls)
print('总耗时:', time.time()-start)