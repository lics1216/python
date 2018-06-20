#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

# 创建Socket时，SOCK_DGRAM指定了这个Socket的类型是UDP。AF_INET指定使用IPv4协议
# 绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据：

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口:
s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999...')

while True:
    # 没写多线程
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    reply = 'Hello, %s!' % data.decode('utf-8')
    s.sendto(reply.encode('utf-8'), addr)