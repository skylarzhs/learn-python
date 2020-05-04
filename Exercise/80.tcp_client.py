#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import socket
# import ssl

# # s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s = ssl.wrap_socket(socket.socket())

# s.connect(('www.sina.com.cn',443))

# s.send(b'GET / HTTP/1.1 \r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# buffer = []
# while True:
#     d = s.recv(1024) #接收数据时，调用recv(max)方法，一次最多接收指定的字节数，因此，在一个while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环。
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)

# print(data)

# s.close()

# header,html = data.split(b'\r\n\r\n',1)
# print(header.decode('utf-8'))

# with open('sina.html','wb') as f:
#     f.write(html)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
s.recv(1024).decode('utf-8')

for data in [b'AA', b'BB', b'CC']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))

s.send(b'exit')

s.close()
