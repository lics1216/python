# -*- coding: utf-8 -*-

# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

# 要注意定义可变参数和关键字参数的语法：

# *args是可变参数，args接收的是一个tuple；

# **kw是关键字参数，kw接收的是一个dict。

# 以及调用函数时如何传入可变参数和关键字参数的语法：

# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。

def print_scores(**kw):   #**代表的是 关键字参数，传入的是 字典类型 dict  用{ } 表示
    print('      Name  Score')
    print('------------------')
    for name, score in kw.items():
        print('%10s  %d' % (name, score))
    print()

print_scores(Adam=99, Lisa=88, Bart=77)  

# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

data = {
    'Adam Lee': 99,
    'Lisa S': 88,
    'F.Bart': 77
}

print_scores(**data)

def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()

print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai', age=18)

# 可变参数的例子
def hello(greeting, *args):
    if (len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args))) 

# 'sep'.join(seq)
# sep：分隔符。可以为空
# seq：要连接的元素序列、字符串、元组、字典
# 上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串

hello('Hi') # => greeting='Hi', args=()
hello('Hi', 'Sarah') # => greeting='Hi', args=('Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam') # => greeting='Hello', args=('Michael', 'Bob', 'Adam')

names = ('Bart', 'Lisa')
hello('Hello', *names) # => greeting='Hello', args=('Bart', 'Lisa')