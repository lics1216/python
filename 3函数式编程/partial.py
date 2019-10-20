# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

int2 = functools.partial(int, base=2)

print('1000000 =', int2('1000000'))
print('1010101 =', int2('1010101'))