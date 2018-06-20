#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
spiderThreadPool.py by lcs
"""
import queue
import threading
import redis
from ..utils import ConstantEnum
from ..instances import FetchHtml, Parser, Saver
class SpiderThreadPool(object):
    # 构造方法
    def __init__(self):
        # 队列，queue.PriorityQueue()这是声明一个优先级队列，put时设置元素优先级，级别越低，get是越先出来
        # 0 代表queque 大小无限制
        self._queue_fetch = queue.Queue(0)
        self._queue_parse = queue.Queue(0)
        self._queue_save = queue.Queue(0)

        # 线程list
        self._thread_fetch_list = []
        self._thread_parse_list = []
        self._thread_save_list = []

        # 记录队列任务个数的变量
        self._number_dict = {
            ConstantEnum.Fetch_Html_not : 0,
            ConstantEnum.Parse_Html_not : 0,
            ConstantEnum.Save_Item_not : 0,
        }

        # 定义操作上面变量的锁
        self._lock = threading.Lock()
        # redis
        self._r = redis.StrictRedis(host='127.0.0.1', port=6379)
    # 调用此方法 开始启动多个线程， FetchHtml(x,y) x代表线程名字，self 是把当前的pool对象传给FetchHtml，供它来操作队列
    def start_work(self):
        self._thread_fetch_list = [FetchHtml("fetchhtml-%s" % (x+1), self) for x in range(5)]
        self._thread_parse_list = [Parser("parsehtml-%s" % (x+1), self) for x in range(2)]
        self._thread_save_list = [Saver("saveitem-%s" % (x+1), self._r, self) for x in range(1)]

        # 启动 fetch线程，parse线程， 启动save
        for th in self._thread_fetch_list:
            th.setDaemon(True)
            th.start()

        for th in self._thread_parse_list:
            th.setDaemon(True)
            th.start()

        for th in self._thread_save_list:
            th.setDaemon(True)
            th.start()
        return

    def wait_finish(self):
        # for th in self._thread_fetch_list:
        #    if th.is_alive():
        #        th.join()
        #
        # for th in self._thread_parse_list:
        #    if th.is_alive():
        #        th.join()
        #
        # for th in self._thread_save_list:
        #    if th.is_alive():
        #        th.join()
        self._queue_fetch.join()
        self._queue_parse.join()
        self._queue_save.join()

    # fetch parser save 实例调用下面的方法 得到一个任务，提交任务，完成任务
    def get_a_task(self, task_name):
        if task_name == ConstantEnum.Fetch_Html:
            # 根据 task_name 取出任务 block 默认为True， 若队列为空，则使得调用线程阻塞

            task_content = self._queue_fetch.get(block=True, timeout=5)
            # 更新 _number_dict 中的 fetch_html_not 数值
            self.update_number_dict(ConstantEnum.Fetch_Html_not, -1)
        elif task_name == ConstantEnum.Parse_Html:
            task_content = self._queue_parse.get(block=True, timeout=5)
            self.update_number_dict(ConstantEnum.Parse_Html_not, -1)
        elif task_name == ConstantEnum.Save_Item:
            task_content = self._queue_save.get(block=True, timeout=5)
            self.update_number_dict(ConstantEnum.Save_Item_not, -1)
        return task_content

    def add_a_task(self, task_name, task_content):
        if task_name == ConstantEnum.Fetch_Html:
            self._queue_fetch.put_nowait(task_content)
            self.update_number_dict(ConstantEnum.Fetch_Html_not, 1)
        elif task_name == ConstantEnum.Parse_Html:
            self._queue_parse.put_nowait(task_content)
            self.update_number_dict(ConstantEnum.Parse_Html_not, 1)
        elif task_name == ConstantEnum.Save_Item:
            self._queue_save.put_nowait(task_content)
            self.update_number_dict(ConstantEnum.Save_Item_not, 1)
        return

    def finish_a_task(self, task_name):
        if task_name == ConstantEnum.Fetch_Html:
            self._queue_fetch.task_done()
        elif task_name == ConstantEnum.Parse_Html:
            self._queue_parse.task_done()
        elif task_name == ConstantEnum.Save_Item:
            self._queue_save.task_done()
        return

    # ===================================================================
    # 调用此方法来更新 _number_dict 的数据，修改时必须开启互斥锁
    def update_number_dict(self, key, value):
        self._lock.acquire()
        self._number_dict[key] += value
        self._lock.release()
        return


    def get_number_dict(self):
        return self._number_dict

    def get_queue(self):
        return [self._queue_fetch, self._queue_parse, self._queue_save]

