# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。


# 可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。

# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_odd(n):
    return n % 2 == 1

L = range(100)

# 例如，在一个list中，删掉偶数，只保留奇数，可以这么写：
# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素

print(list(filter(is_odd, L))) # 注意到 返回的Iterator是惰性计算的序列, 用list() 处理

def not_empty(s):
    return s and s.strip()  

    # str.strip([chars]);
    # chars -- 移除字符串头尾指定的字符。
    # 返回移除字符串头尾指定的字符生成的新字符串

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

# ############################# 没看代码

def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

if __name__ == '__main__':
    main()