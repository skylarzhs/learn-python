# -*- coding : utf-8 -*-

# 定义自己的abs

# def my_abs(x):
#     if x>=0:
#         return x
#     else:
#         return -x


# 空函数

# def nop():
#     pass

# 参数检查

# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     if x>=0:
#         return x
#     else:
#         return -x

# n = input('Please enter a number:\r\n')

# # n = int(n)

# print('您输入的数值为 %s,计算得到绝对值为 %s' % (n,my_abs(n)))

import math


# def move(x, y, step, angle=0):
#     nx = x + step*math.cos(angle)
#     ny = y - step*math.sin(angle)
#     return nx, ny


# x, y = move(100, 100, 60, math.pi/6)

# print(x, y)

# r = move(100, 100, 60, math.pi/6)

# print(r)

# 课后题，计算一元二次方程的根

def quadratic(a, b, c):
    # 参数检查
    if not isinstance(a, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(b, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(c, (int, float)):
        raise TypeError('bad operand type')
    # 计算
    temp = math.sqrt(b*b-4*a*c)
    x1 = (-b + temp)/(2*a)
    x2 = (-b - temp)/(2*a)

    return x1, x2


print(quadratic(1, 2, 1))
