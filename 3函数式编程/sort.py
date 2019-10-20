# sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。
 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key=str.lower)) 
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。对比原始的list和经过key=abs处理过的list：
# list = [36, 5, -12, 9, -21]

# keys = [36, 5,  12, 9,  21]
# 然后sorted()函数按照keys进行排序，并按照对应关系返回list相应的元素：

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

#  #######  没看代码
print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))