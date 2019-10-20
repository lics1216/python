# Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较

# value属性则是自动赋给成员的int常量，默认从1开始计数。

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon

print('day1 =', day1)
print('Weekday.Tue =', Weekday.Tue)
print('Weekday[\'Tue\'] =', Weekday['Tue'])
print('Weekday.Tue.value =', Weekday.Tue.value)
print('day1 == Weekday.Mon ?', day1 == Weekday.Mon)
print('day1 == Weekday.Tue ?', day1 == Weekday.Tue)
print('day1 == Weekday(1) ?', day1 == Weekday(1))

for name, member in Weekday.__members__.items():
    print(name, '=>', member)

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)