# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，
# 它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：

# >>> dir('ABC')
# ['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']

# #######################################

# 但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：
# class Student(object):
#     name = 'Student'
# 当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。来测试一下：

# >>> class Student(object):
# ...     name = 'Student'
# ...
# >>> s = Student() # 创建实例s
# >>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
# Student
# >>> print(Student.name) # 打印类的name属性
# Student
# >>> s.name = 'Michael' # 给实例绑定name属性
# >>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
# Michael
# >>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
# Student
# >>> del s.name # 如果删除实例的name属性
# >>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
# Student

# 从上面的例子可以看出，在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，
# 因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性