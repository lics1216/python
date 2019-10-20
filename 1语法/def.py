# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0
# 的两个解。
# 提示：计算平方根可以调用math.sqrt()函数：


# 总结：
# 定义函数时，需要确定函数名和参数个数；
# 如果有必要，可以先对参数的数据类型做检查；
# 函数体内部可以用return随时返回函数结果；
# 函数执行完毕也没有return语句时，自动return None。
# 函数可以同时返回多个值，但其实就是一个tuple。

# import math

# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny

# >>> x, y = move(100, 100, 60, math.pi / 6)
# >>> print(x, y)
# 151.96152422706632 70.0


# -*- coding: utf-8 -*-

import math

# 绝对值
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
# 数学计算
def move(x, y, step, angle=0):   
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

# 输入 一元二次方程系数：a,b,c   输出解  本次编写函数过程中 特别注意 tab 和 空格符 indentationError   
# angle 是默认参数，其间涉及到参数类型知识点,一定得设置 tab 默认为4个空格
# 参考连接 http://www.cnblogs.com/freeweb/p/5814369.html
def quadratic(a,b,c):
    if not isinstance(a,(int,float)) or not isinstance(a,(int,float)) or not isinstance(a,(int,float)):
        raise TypeError("参数必须是整型 或者 float")
    d = b*b - a*c
    if d < 0:
        print("方程在 实数域 内无解")
    elif d == 0:
        print("result:",-b/2*a)
    else:
        r1 = (-b - d) / 2*a
        r2 = (-b + d) / 2*a
        print("解1：",r1)   #复制行快捷键： ctrl + shift + D
        print("解2：",r2)


# n = my_abs(-20)
# print(n)

# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)

# # TypeError: bad operand type:
# my_abs('123')

quadratic(3,5,2)
