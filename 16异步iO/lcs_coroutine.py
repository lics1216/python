# 看起来A、B的执行有点像多线程，但协程的特点在于是一个线程执行，那和多线程比，协程有何优势？

# 最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，
# 因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。

# 第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，
# 在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。

# 因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，
# 既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。

# Python对协程的支持是通过generator实现的。

# 在generator中，我们不但可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值。

# 但是Python的yield不但可以返回一个值，它还可以接收调用者发出的参数。

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 我们再来看另外一个非常重要的函数send(msg)。其实next()和send()在一定意义上作用是相似的，
# 区别是send()可以传递yield表达式的值进去，而next()不能传递特定的值，
# 只能传递None进去。因此，我们可以看做c.next() 和 c.send(None) 作用是一样的。

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None) # 和next()在用相当
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)  # send(n) 把n赋值给consumer()的n，并且返回 yield 后面的当前r给 r
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)


# 注意到consumer函数是一个generator，把一个consumer传入produce后：
# 首先调用c.send(None)启动生成器；
# 然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
# consumer通过yield拿到消息，处理，又通过yield把结果传回；
# produce拿到consumer处理的结果，继续生产下一条消息；
# produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
# 整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
# 最后套用Donald Knuth的一句话总结协程的特点：
# “子程序就是协程的一种特例。