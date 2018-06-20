# Base64的原理很简单，首先，准备一个包含64个字符的数组：
# 然后，对二进制数据进行处理，每3个字节一组，一共是3x8=24bit，划为4组，每组正好6个bit：

# 还可以自己定义64个字符的排列顺序，这样就可以自定义Base64编码，不过，通常情况下完全没有必要。

# Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。

# Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。

# 由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64

s = base64.b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.b64decode(s).decode('utf-8')
print(d)

s = base64.urlsafe_b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.urlsafe_b64decode(s).decode('utf-8')
print(d)