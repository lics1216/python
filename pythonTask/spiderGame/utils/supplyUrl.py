#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
SupplyUrl.py by lcs
"""
import threading
import json, random, time
import logging
from urllib import request
from bs4 import BeautifulSoup
from ..utils import ConstantEnum

class SupplyUrl(threading.Thread):
    def __init__(self, name, pool):
        threading.Thread.__init__(self, name=name)
        self._pool = pool
    """
     queue() put的时候，不用调用task_done, 每个put进入queue的元素都有一个task_done
    """
    def run(self):
        print("%s, 正在启动" %threading.current_thread().name)
        # 获取游戏的首页面
        hrefs = self.get_gameSort_startHref()
        for x in hrefs:
            if(self._pool.get_number_dict()[ConstantEnum.Fetch_Html_not] > 300):
                time.sleep(3)  # 该时间别超过 socket 设置的defaulttimeout(),否则ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接
            self.get_game_Href(x)
        return

    # 获取游戏种类的首页面，比如策略类游戏的首页
    def get_gameSort_startHref(self):
        # 设置代理
        ips = ["http://183.60.178.21:60100", "http://183.60.178.22:60100", "http://219.135.99.85:60100","http://219.135.99.88:60100", "http://219.135.99.89:60100", "http://219.135.99.90:60100","http://219.135.99.91:60100", "http://219.135.99.92:60100", "http://219.135.99.93:60100", "http://219.135.99.94:60100"]
        proxies = "{\'https\':\'"+ ips[random.randint(0, len(ips)-1) ] +"\'}"
        proxy = request.ProxyHandler(eval(proxies))
        opener =request.build_opener(proxy, request.HTTPHandler)
        request.install_opener(opener)
        # 开始请求
        with request.urlopen("https://www.taptap.com/categories") as f:
            html = f.read().decode('utf-8')
            soup = BeautifulSoup(html, "html.parser")
            # print(soup)
            # 发现 ul class="list-unstyled category-tags"
            link = soup.find_all("ul", attrs={"class": "list-unstyled category-tags"})[0]
            link = link.find_all("a")
            # 第一个是新游预约，忽略。 -1，取出href 链接的,/ 最后的一个数据
            hrefs = [x.attrs['href'].split('/')[-1] for x in link[1:len(link)]]

            # 处理成能进行再分类处爬取的链接
            # 策略
            # https://www.taptap.com/tag/%E7%AD%96%E7%95%A5
            # https://www.taptap.com/ajax/search/tags?&kw=%E7%AD%96%E7%95%A5&sort=hits&page=1
            # 动作
            # https://www.taptap.com/tag/%E5%8A%A8%E4%BD%9C
            # https://www.taptap.com/ajax/search/tags?&kw=%E5%8A%A8%E4%BD%9C&sort=hits&page=1
            hrefs = ['https://www.taptap.com/ajax/search/tags?&kw=' + x + '&sort=hits&page=1' for x in hrefs]
        return hrefs

    # 获取每一个游戏的 链接如，https://www.taptap.com/app/49995, 并写入到 pool的 fetch_queue 队列
    def get_game_Href(self, gameSort_startHref):
        # 设置代理
        ips = ["http://183.60.178.21:60100", "http://183.60.178.22:60100", "http://219.135.99.85:60100","http://219.135.99.88:60100", "http://219.135.99.89:60100", "http://219.135.99.90:60100","http://219.135.99.91:60100", "http://219.135.99.92:60100", "http://219.135.99.93:60100", "http://219.135.99.94:60100"]
        proxies = "{\'https\':\'"+ ips[random.randint(0, len(ips)-1) ] +"\'}"
        proxy = request.ProxyHandler(eval(proxies))
        opener =request.build_opener(proxy, request.HTTPHandler)
        request.install_opener(opener)
        # 开始请求
        with request.urlopen(gameSort_startHref) as f:
            # html 一个 json 字符串
            html = json.loads(f.read().decode('utf-8'))
            # print(html['data']['html'])
            # print("next:",html['data']['next'])
            # json 的 html 是否为空
            if not html['data']['html'] is '' and not html['data']['next'] is None:
                soup = BeautifulSoup(html['data']['html'], "html.parser")
                # 可以考虑递归
                nextLink = html['data']['next']
                # 输出规格化soup ，展示html格式，这是为了开发人看，不是给python解释器看，它无所谓的！
                #  print(soup.prettify())

                # game_url a class="app-card-left"  为什么 attrs['href'] 用中括号，而不是（）
                link = soup.find_all('a', attrs={'class': 'app-card-left'})
                gameHref = [x.attrs['href'] for x in link]
                # print(gameHref)
                # 加入抓取 gameHref 指定游戏信息的代码
                for x in gameHref:
                    # 把 游戏链接 x， 添加task 到 queue_fetch
                    self._pool.add_a_task(ConstantEnum.Fetch_Html, x)
                self.get_game_Href(nextLink)
            else:
                logging.info("------------------------一种游戏全部 hrefs 写入queue_fetch完毕-------------------------")
                pass
