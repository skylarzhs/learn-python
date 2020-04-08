# -*- coding : utf-8 -*-

# 定义自己的abs

# def my_abs(x):
#     if x>=0:
#         return x
#     else:
#         return -x

# 参数检查

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x
