# map reduce 和 hadoop 的mapreduce 处理思想类似，

# mapReduce 用来 处理wordCount 的例子， map函数接受 键值对  key:文件名  value: 文件内容  
# 利用 map 对很多文件分片统计 字符出现的次数，返回 键值对。
# reduce 接受键值对，统计相同key值(字符相同)的 value 之和！


# python的 map 接受一个函数 f, 一个list数据类型。使得每一个 f 作用于 list的每一个元素
# list 的每一个元素 看成是文件分片，f来处理分片, map 返回一个 iterate 

# reduce 接受一个函数f, 一个list
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

def f(x):
    return x * x

print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
print(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]))  # map() 返回一个 iterate

# 不用 map
# L = []
# for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     L.append(f(n))
# print(L)

# #########################  reduce 
CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

# str转成 int
def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)

print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))


