#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    # reader writer 用来干嘛的
    reader, writer = yield from connect 
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# ############### 返回结果
# wget www.sina.com.cn...
# wget www.163.com...
# wget www.sohu.com...
# www.sohu.com header > HTTP/1.1 200 OK
# www.sohu.com header > Content-Type: text/html;charset=UTF-8
# www.sohu.com header > Connection: close
# www.sohu.com header > Server: nginx
# www.sohu.com header > Date: Thu, 19 Apr 2018 09:38:27 GMT
# www.sohu.com header > Cache-Control: max-age=60
# www.sohu.com header > X-From-Sohu: X-SRC-Cached
# www.sohu.com header > Content-Encoding: gzip
# www.sohu.com header > FSS-Cache: HIT from 8878809.15760099.10215
# www.sohu.com header > FSS-Proxy: Powered by 3373701.4749967.4710
# www.163.com header > HTTP/1.0 302 Moved Temporarily
# www.163.com header > Server: Cdn Cache Server V2.0
# www.163.com header > Date: Thu, 19 Apr 2018 09:38:32 GMT
# www.163.com header > Content-Length: 0
# www.163.com header > Location: http://www.163.com/special/0077jt
# www.163.com header > Connection: close
# www.sina.com.cn header > HTTP/1.1 200 OK
# www.sina.com.cn header > Server: nginx
# www.sina.com.cn header > Date: Thu, 19 Apr 2018 09:38:32 GMT
# www.sina.com.cn header > Content-Type: text/html
# www.sina.com.cn header > Content-Length: 602912
# www.sina.com.cn header > Connection: close
# www.sina.com.cn header > Last-Modified: Thu, 19 Apr 2018 09:36:4
# www.sina.com.cn header > Vary: Accept-Encoding
# www.sina.com.cn header > X-Powered-By: shci_v1.03
# www.sina.com.cn header > Expires: Thu, 19 Apr 2018 09:39:21 GMT
# www.sina.com.cn header > Cache-Control: max-age=60
# www.sina.com.cn header > Age: 2
# www.sina.com.cn header > Via: http/1.1 ctc.ningbo.ha2ts4.97 (Apa
# /6.2.1 [cHs f ]), http/1.1 ctc.xiamen.ha2ts4.41 (ApacheTrafficSe
# f ])
# www.sina.com.cn header > X-Via-Edge: 15241307124554c9b87db3cd64c
# www.sina.com.cn header > X-Cache: HIT.41
# www.sina.com.cn header > X-Via-CDN: f=edge,s=ctc.xiamen.ha2ts4.4
# m,c=219.135.155.76;f=Edge,s=ctc.xiamen.ha2ts4.41,c=222.76.214.43