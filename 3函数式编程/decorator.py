# 在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，
# 而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。

# decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。




# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
# 但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）



# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。


#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 函数对象有一个__name__属性，可以拿到函数的名字：

# >>> now.__name__
# 'now'
# >>> f.__name__
# 'now'

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()

def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('DEBUG')
def today():
    print('2015-3-25')

today()
print(today.__name__)