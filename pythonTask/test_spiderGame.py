#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
test_spiderGame.py  by lcs   下面的from 若写成， .spiderGame 是不行的
"""
import time
from spiderGame import tapSpider,  SupplyUrl

def test():

   spider = tapSpider()
   supplyurl = SupplyUrl("supplyUrl-thread-01", spider)

   # 启动supplyurl， spider里面的线程
   supplyurl.setDaemon(True)
   supplyurl.start()
   # 给 supplyurl 线程一些时间，往queue_fecth 写数据
   time.sleep(10)

   # 启动 fetch parser saver 三个线程
   spider.start_work()

   # join 想通过 三个队列 queue  join() 来控制
   spider.wait_finish()

   # supplyurl.join()



if __name__ == '__main__':
    import socket
    socket.setdefaulttimeout(5)
    test()

