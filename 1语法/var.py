#请打印出以下变量的值：

# -*- coding: utf-8 -*-
# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Lisa!'''

# 总结区别：
#    对变量赋值x = y是把变量x指向真正的对象，该对象是变量y所指向的。随后对变量y的赋值不影响变量x的指向。

#    注意：Python的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的，例如Java对32位整数的范围限制在-2147483648-2147483647。

#    Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。

print("n =",123)

print("f = ",456.789)   #逗号代表，空格  ，最后可以不用加分号!

print("s1 =", "'Hello, world'")

print("s2 =", "'Hello, \\'Adam\\''")  

print("s3 =","r'Hello, \"Bart\"'")

print("s4 = ","r'''Hello")

print("Lisa!'''")

print(r'\\\\\\\\t')  # r'dsfsd\\\sdfd\\'    '' 里面的字符串默认不转义
