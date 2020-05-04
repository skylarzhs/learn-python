#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import socket
import threading
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',9999))

s.listen(5)
print('waiting for connection...')

def tcplink(sock,addr):
    print('Accept new connection from %s:%s' % addr)
    sock.send(b'welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


while True:
    sock,addr = s.accept()
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()
    print(threading.current_thread(),'name : %s' % threading.current_thread().name)

# Accept new connection from 127.0.0.1:49188
# <_MainThread(MainThread, started 7228)> name : MainThread
# Connection from 127.0.0.1:49186 closed.
# Accept new connection from 127.0.0.1:49192
# <_MainThread(MainThread, started 7228)> name : MainThread
# Connection from 127.0.0.1:49188 closed.
# Connection from 127.0.0.1:49192 closed.
# Accept new connection from 127.0.0.1:49386
# <_MainThread(MainThread, started 7228)> name : MainThread
# Accept new connection from 127.0.0.1:49390
# <_MainThread(MainThread, started 7228)> name : MainThread
# Connection from 127.0.0.1:49386 closed.
# Accept new connection from 127.0.0.1:49392
# <_MainThread(MainThread, started 7228)> name : MainThread
# Connection from 127.0.0.1:49390 closed.
# Accept new connection from 127.0.0.1:49395
# <_MainThread(MainThread, started 7228)> name : MainThread
# Connection from 127.0.0.1:49392 closed.
# Accept new connection from 127.0.0.1:49400
# <_MainThread(MainThread, started 7228)> name : MainThread
# Connection from 127.0.0.1:49395 closed.