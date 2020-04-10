#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import random
import time
import queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()

# 从 BaseManager 继承的 QueueManager


class QueueManager(BaseManager):
    pass


# 把两个Queue都注册到网络上，callable参数关联了Queue对象
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

# 绑定5000端口，设置验证码‘abc’
manager = QueueManager(address=('', 5000), authkey=b'abc')

# 启动Queue
manager.start()
# 获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...', n)
    task.put(n)
# 从result队列读取结果
print('Try get result...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result : %s' % r)

# close
manager.shutdown()
print('master exit')

# --| Put task %d... 9617
# --| Put task %d... 6050
# --| Put task %d... 8424
# --| Put task %d... 7709
# --| Put task %d... 4353
# --| Put task %d... 8875
# --| Put task %d... 7521
# --| Put task %d... 8250
# --| Put task %d... 4891
# --| Put task %d... 9276
# --| Try get result...
# --| Result : 9617 * 9617 = 92486689
# --| Result : 6050 * 6050 = 36602500
# --| Result : 8424 * 8424 = 70963776
# --| Result : 7709 * 7709 = 59428681
# --| Result : 4353 * 4353 = 18948609
# --| Result : 8875 * 8875 = 78765625
# --| Result : 7521 * 7521 = 56565441
# --| Result : 8250 * 8250 = 68062500
# --| Result : 4891 * 4891 = 23921881
# --| Result : 9276 * 9276 = 86044176
# --| master exit

# 当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，但是，在分布式多进程环境下，添加任务到Queue不可以直接对原始的task_queue进行操作，那样就绕过了QueueManager的封装，必须通过manager.get_task_queue()获得的Queue接口添加。