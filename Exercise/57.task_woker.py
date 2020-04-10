#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import time
import sys
import queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行task_master.py的机器
server_addr = '192.168.56.13'
print('Connect to server %s...' % server_addr)

# 端口和验证码注意保持与task_master设置的一致
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 从网络连接
m.connect()
# 获取Queue对象
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列获取任务，并把结果写入result队列
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task queue is empty.')

print('worker exit.')

# --| Connect to server 127.0.0.1...
# --| run task 9617 * 9617
# --| run task 6050 * 6050
# --| run task 8424 * 8424
# --| run task 7709 * 7709
# --| run task 4353 * 4353
# --| run task 8875 * 8875
# --| run task 7521 * 7521
# --| run task 8250 * 8250
# --| run task 4891 * 4891
# --| run task 9276 * 9276
# --| worker exit.

# 测试：虚拟机开master，本机winworker，再增加虚拟机worker，master正常运行，worker执行后报错

# master
# --| Put task %d... 5047
# --| Put task %d... 7950
# --| Put task %d... 5799
# --| Put task %d... 1163
# --| Put task %d... 7468
# --| Put task %d... 7757
# --| Put task %d... 1857
# --| Put task %d... 8241
# --| Put task %d... 9338
# --| Put task %d... 7146
# --| Try get result...
# --| Result : 5047 * 5047 = 25472209
# --| Result : 7950 * 7950 = 63202500
# --| Result : 5799 * 5799 = 33628401
# --| Result : 1163 * 1163 = 1352569
# --| Result : 7468 * 7468 = 55771024
# --| Result : 7757 * 7757 = 60171049
# --| Result : 1857 * 1857 = 3448449
# --| Result : 8241 * 8241 = 67914081
# --| Result : 9338 * 9338 = 87198244
# --| Result : 7146 * 7146 = 51065316
# --| master exit

# win - worker
# --| Connect to server 192.168.56.13...
# --| run task 5047 * 5047
# --| run task 7950 * 7950
# --| run task 5799 * 5799
# --| run task 1163 * 1163
# --| run task 7468 * 7468
# --| run task 7757 * 7757
# --| run task 1857 * 1857
# --| run task 9338 * 9338
# --| Traceback (most recent call last):
# --|   File ".\Exercise\57.task_woker.py", line 32, in <module> line 32, in <module>
# --|     n = task.get(timeout=1)
# --|   File "<string>", line 2, in get    b\multiprocessing\managers.py", line 835, in
# --|   File "D:\Program Files\Python3.8\lib\multiprocessing\managers.py", line
# --| 835, in _callmethod                  b\multiprocessing\connection.py", line 250,
# --|     kind, result = conn.recv()
# --|   File "D:\Program Files\Python3.8\lib\multiprocessing\connection.py", linb\multiprocessing\connection.py", line 414,e 250, in recv
# --|     buf = self._recv_bytes()
# --|   File "D:\Program Files\Python3.8\lib\multiprocessing\connection.py", line 383,b\multiprocessing\connection.py", line 414, in _recv_bytes
# --|     buf = self._recv(4)
# --|   File "D:\Program Files\Python3.8\lib\multiprocessing\connection.py", line 383,
# --| in _recv
# --|     raise EOFError
# --| EOFError

# vm - worker
# --| Connect to server 127.0.0.1...
# --| run task 8241 * 8241
# --| run task 7146 * 7146
# --| Traceback (most recent call last):
# --|   File "Exercise/57.task_woker.py", line 32, in <module>
# --|     n = task.get(timeout=1)
# --|   File "<string>", line 2, in get
# --|   File "/usr/local/python3.8/lib/python3.8/multiprocessing/managers.py", line 835, in _callmethod
# --|     kind, result = conn.recv()
# --|   File "/usr/local/python3.8/lib/python3.8/multiprocessing/connection.py", line 250, in recv
# --|     buf = self._recv_bytes()
# --|   File "/usr/local/python3.8/lib/python3.8/multiprocessing/connection.py", line 414, in _recv_bytes
# --|     buf = self._recv(4)
# --|   File "/usr/local/python3.8/lib/python3.8/multiprocessing/connection.py", line 383, in _recv
# --|     raise EOFError
# --| EOFError