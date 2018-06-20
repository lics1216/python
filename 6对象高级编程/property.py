# @property广泛应用在类的定义中，可以让调用者写出简短的代码，
# 同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性

# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：


# 有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？
# 对于追求完美的Python程序员来说，这是必须要做到的！

# 还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。
# Python内置的@property装饰器就是负责把一个方法变成属性调用的：

# 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，
# 负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：


class Screen(object):
     
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        if not isinstance(value,(int,float)):
            raise ValueError('score must be an integer!')
        self._width = value

    @property
    def height(self):
        return self._heigth

    @width.setter
    def height(self,value):
        if not isinstance(value,(int,float)):
            raise ValueError('score must be an integer!')
        self._heigth = value


    @property
    def resolution(self):
        return 2000


s = Screen()
s.width = 100.9
s.height = 9090
print("屏幕 宽 为", s.width)
print("屏幕 heigth 为 %d"  % (s.height))
print(s.resolution)


