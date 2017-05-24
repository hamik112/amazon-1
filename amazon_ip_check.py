# -*- coding: utf-8 -*-
from amazon_store import AmazonIpStore
import random
from settings import HEADERS
import requests
from lxml import etree
from threading import Thread, RLock
import Queue
import traceback
import json
import time

message = ''  # 状态
products = ['apple', 'adidas', 'nike', 'lenovo', 'xiaomi', 'oneplus']


class MyThread(Thread):
    def __init__(self, queue):
        super(MyThread, self).__init__()
        self.queue = queue

    def run(self):
        while 1:
            if self.queue.empty():
                break
            else:
                ip_check()


def get_ip_list(ip_url):
    res = requests.get(ip_url)
    res_code = json.loads(res.text)['code']
    while res_code == -51:
        res = requests.get(ip_url)
        res_code = json.loads(res.text)['code']
    return json.loads(res.text)['data']['proxy_list']


def ip_check():
    global message, num
    ip_choice = que.get()
    proxies = {"http": 'http://' + ip_choice}
    headers = {
        "User-Agent": random.choice(HEADERS)
    }
    kw = random.choice(products)
    url = 'https://www.amazon.com/s/ref=nb_sb_noss?field-keywords==%s' % kw
    try:
        t1 = time.time()
        res = requests.get(url, proxies=proxies, headers=headers, timeout=5)
        result = etree.HTML(res.content)
        search_word = result.xpath('//input[@id="twotabsearchtextbox"]')
        if len(search_word) > 0:
            t2 = time.time()
            t = int((t2-t1)*1000)
            lock1.acquire()
            amazon_ip.insert_info(ip_choice, t, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            message = u'可用存库'
            lock1.release()
        else:
            message = u'不可用'
    except:
        #traceback.print_exc()
        message = u'超时'
    finally:
        que.task_done()
        lock.acquire()
        num -= 1
        print message, num
        lock.release()


if __name__ == '__main__':

    #ip_100 = 'http://dev.kuaidaili.com/api/getproxy/?orderid=937340558535151&num=500&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=1&method=2&an_ha=1&sp1=1&sp2=1&sp3=1&sort=1&format=json&sep=1'
    # 高匿
    ip_100 = 'http://dev.kuaidaili.com/api/getproxy/?orderid=937340558535151&num=1000&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=1&method=2&an_ha=1&quality=1&format=json&sep=1'
    proxy_list = get_ip_list(ip_100)

    try:
        amazon_ip = AmazonIpStore()
    except:
        print u'连接数据库错误'

    num = len(proxy_list)
    print u'待验证ip数量：%s' % num

    lock = RLock()
    lock1 = RLock()

    que = Queue.Queue()
    [que.put(proxy) for proxy in proxy_list]

    threads = [MyThread(que) for i in range(30)]
    [thread.start() for thread in threads]

    que.join()
    time.sleep(1)
    print u'验证完毕'









