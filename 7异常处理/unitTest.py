# 单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。
# 单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。
# 单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。
# 单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。


# 我们来编写一个Dict类，这个类的行为和dict一致，但是可以通过属性来访问，用起来就像下面这样：

class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


# 为了编写单元测试，我们需要引入Python自带的unittest模块，编写mydict_test.py如下：
# 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。

# 对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，
# 我们只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是assertEqual()

import unittest

# from mydict import Dict

class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':        #  这么写什么意思？  
    unittest.main()


# 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
# setUp()和tearDown()方法有什么用呢？设想你的测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库，
# 在tearDown()方法中关闭数据库，这样，不必在每个测试方法中重复相同的代码：

# class TestDict(unittest.TestCase):

#     def setUp(self):
#         print('setUp...')

#     def tearDown(self):
#         print('tearDown...')
# 可以再次运行测试看看每个测试方法调用前后是否会打印出setUp...和tearDown...。 