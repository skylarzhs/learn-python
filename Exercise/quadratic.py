# -*- encoding : utf-8 -*-

import math

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

# 1. 函数的定义名称有响应的语义
# 2. 参数检查必不可少
# 3. 先要确保逻辑正确，1+1=2
# 4. 问题：在命令行使用import加载函数，在目录下生成__pycache__文件夹quadratic.cpython-38.pyc文件。
# 文件改动不会自动加载修改后的文件，需要退出命令行重新进入后才会重新加载。
# 网上查的资源都是进行模块加载，应用于函数不起作用，reload() argument must be a module，问题先记录。
