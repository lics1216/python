#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
saver.py by lcs
"""
import threading
from ..utils import ConstantEnum
class Saver(threading.Thread):
    def __init__(self, name, r, pool):
        threading.Thread.__init__(self, name=name)
        self._r = r
        self._pool = pool
    """
      这个run 方法应该一直执行的
    """
    def run(self):
        print("%s, 正在启动" %threading.current_thread().name)
        while True:
            # 从pool 里面调用save任务，获取item
            data = self._pool.get_a_task(ConstantEnum.Save_Item)

            # save item
            self._r.hmset('game_taptap_' + data.get('game_id'), data)
            print("%s 写入redis" % data.get('game_name'))

            # 完成 取save, finnish save
            self._pool.finish_a_task(ConstantEnum.Save_Item)