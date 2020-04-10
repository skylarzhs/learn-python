#! /usr/bin/env python3
# -*- coding : utf-8 -*-

from multiprocessing import Pool
import os
import time
import random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(5)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocessed done...')
    p.close()
    p.join()
    print('All subprocesses done.')

# Parent process 5064.
# Waiting for all subprocessed done...
# Run task 0 (10124)...
# Run task 1 (7184)...
# Run task 2 (1220)...
# Run task 3 (9012)...
# Task 3 runs 1.14 seconds.
# Run task 4 (9012)...
# Task 0 runs 2.00 seconds.
# Task 2 runs 1.99 seconds.
# Task 1 runs 2.93 seconds.
# Task 4 runs 2.40 seconds.
# All subprocesses done.

# 代码解读：

# 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。

# 请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。如果改成：
# p = Pool(5)
# 就可以同时跑5个进程。