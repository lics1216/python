# 使用key-value存储结构的dict在Python中非常有用，选择不可变对象作为key很重要，最常用的key是字符串。

# tuple虽然是不变对象，但试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果


# -*- coding: utf-8 -*-

#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
#要创建一个set，需要提供一个list作为输入集合：
s1 = set([1, 1, 2, 2, 3, 3])
print(s1)
s2 = set([2, 3, 4])  #调用 add 和 remove 方法

print(s1 & s2)    # s1 s2 的交集
print(s1 | s2)    # s1 s2 的并集

#记住  dict 字典类型使用 {} 表示，，， 
d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))   # key没有的，返回None , 或者自己指定的值 -1


# >>> a = 'abc'
# >>> b = a.replace('a', 'A')
# >>> b            // b是字符串 不可变对象
# 'Abc'
# >>> a
# 'abc'