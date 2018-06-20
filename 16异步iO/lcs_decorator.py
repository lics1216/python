# 函数运行之前打印出其 函数名和 运行时间

import functools
def log(func):
    # 下面这引用的原因，解释比较复杂！查看
    # https://www.liaoxuefeng.com
    @functools.wraps(func) 
    def wrapper(*args, **kw):
        from datetime import datetime
        print("函数%s runtime start: %s" % (func.__name__,datetime.now()))
        return func(*args, **kw)
    return wrapper

@log
def lcs():
    print("李长松测试装饰器")


lcs()