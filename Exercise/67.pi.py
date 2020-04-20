#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import itertools
from functools import reduce

# 利用Python提供的itertools模块，我们来计算这个序列的前N项和


# def pi(N):
#     # ' 计算pi的值 '
#     # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
#     odds = itertools.count(1, 2)
#     # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
#     limit = itertools.takewhile(lambda x: x <= 2*N-1, odds)
#     # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...

#     L = []
#     for k,v in enumerate(limit):
#         if k % 2 ==0:
#             signal = 1
#         else:
#             signal = -1
#         L.append(4 * signal / v)
#     # print(L)
#     pi = reduce(lambda x, y: x+y, L)
#     # step 4: 求和:
#     return pi

def pi(N):
    return sum([(-1) ** (n - 1) * 4 / (n * 2 - 1) for n in itertools.takewhile(lambda i: i <= N, itertools.count(1))])


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
