#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
fetchHtml.py by lcs
"""
import threading
import random, time
import logging
from urllib import request
from ..utils import ConstantEnum

class FetchHtml(threading.Thread):
    logging.basicConfig(filename='./LOG/' + __name__ + '.log',
                        format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.INFO,
                        filemode='a', datefmt='%Y-%m-%d %I:%M:%S %p')

    def __init__(self, name, pool):
        threading.Thread.__init__(self, name=name)
        self._pool = pool
    """
      这个run 方法应该一直执行的
    """
    def run(self):
        print("%s, 正在启动" %threading.current_thread().name)
        while True:
            # 从pool 里面调用Fetch_html任务，获取url
            try:
                url = self._pool.get_a_task(ConstantEnum.Fetch_Html)
            except:
                time.sleep(3)
            # 设置代理
            ips = ["http://183.60.178.21:60100", "http://183.60.178.22:60100", "http://219.135.99.85:60100",
                   "http://219.135.99.88:60100", "http://219.135.99.89:60100", "http://219.135.99.90:60100",
                   "http://219.135.99.91:60100", "http://219.135.99.92:60100", "http://219.135.99.93:60100",
                   "http://219.135.99.94:60100"]
            proxies = "{\'https\':\'" + ips[random.randint(0, len(ips) - 1)] + "\'}"
            proxy = request.ProxyHandler(eval(proxies))
            opener = request.build_opener(proxy, request.HTTPHandler)
            request.install_opener(opener)
            # 获取页面
            with request.urlopen(url) as f:
                try:
                    html = f.read().decode("utf-8")
                except:
                    logging.info(url+",不知道是不是请求超时了!")

            # 添加 parse 任务，内容为html
            self._pool.add_a_task(ConstantEnum.Parse_Html, html)

            # 完成 取Fetch_html 和 添加任务, finnish Fetch_html
            self._pool.finish_a_task(ConstantEnum.Fetch_Html)



