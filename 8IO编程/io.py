# 你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。
# 当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。
# 只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
# 忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

# 这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。

# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，
# 可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，
# 调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。

# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；
# 如果是配置文件，调用readlines()最方便：

with open('test.txt', 'w') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('test.txt', 'r') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)