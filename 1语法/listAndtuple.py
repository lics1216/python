# -*- coding: utf-8 -*-
#  list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]

# # 打印Apple:
# # 打印Python:
# # 打印Lisa:


# [] 表示 list  
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])


#定义 tuple 利用（ ）
t = ('a', 'b', ['A', 'B'])  #  （） 含有 [],表示 tuple 里面含有一个 list
 t[2][0] = 'X'
 t[2][1] = 'Y'

print(t)

