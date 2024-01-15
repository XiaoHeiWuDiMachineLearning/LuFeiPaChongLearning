from multiprocessing import Process
import time

def get_request(url):
    print('正在请求数据', url)
    time.sleep(1)
    print('请求数据结束', url)

if __name__ == '__main__':
    start = time.time()
    urls = ['www.1.com', 'www.2.com', 'www.3.com']
    p_list = []
    for url in urls:
        # 根据指定url进行网络请求发送
        p = Process(target=get_request, args=(url, ))
        p_list.append(p)  # 将子进程添加到p_list
        p.start()

    for p in p_list:
        p.join()    # p_list中每一个子进程都会执行join操作
    print('总耗时:', time.time()-start)