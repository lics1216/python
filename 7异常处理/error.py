# err_logging.py

import logging


try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

# ###############################
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')


# #############################
# 其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。
# 但是，由于当前函数不知道应该怎么处理该错误，
# 所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，
# 就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理


class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')