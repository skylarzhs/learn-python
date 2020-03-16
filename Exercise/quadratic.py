# -*- encoding : utf-8 -*-

def quadratic(a, b, c):
    import math
    # 参数检查
    if not isinstance(a, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(b, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(c, (int, float)):
        raise TypeError('bad operand type')
    # 计算
    temp = math.sqrt(b*b-4*a*c)
    x1 = -b + temp
    x2 = -b - temp

    return x1,x2
