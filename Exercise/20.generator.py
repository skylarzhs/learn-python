# -*- coding:utf-8 -*-

# 斐波那契数列 （Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...


# def fib(max):
#     L = [1]
#     if max == 1:
#         return L
#     else:
#         L.append(1)
#     i = 2
#     while i < max:
#         L.append(L[i-2] + L[i-1])
#         i = i + 1
#     return L


# print(fib(1))
# print(fib(1))
# print(fib(10))

# 原版

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a+b
#         n = n + 1
#     return 'done'

# 修改为generator


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'

# >>> def odd():
# ...     print('step 1')
# ...     yield 1
# ...     print('step 2')
# ...     yield 2
# ...     print('step 3')
# ...     yield 3
# ...
# >>> o = odd()
# >>> o
# <generator object odd at 0x00000201B17E14A0>
# >>> next(o)
# step 1
# 1
# >>> next(o) ##### 从上次yield的地方开始执行
# step 2
# 2
# >>> next(o)
# step 3
# 3
# >>> next(o)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

# f = fib(6)

# for n in f:
#     print(n)

# while True:
#     try:
#         x = next(f)
#         print('f:',x)
#     except StopIteration as e:
#         print(e.value)
#         break


# 练习
# 杨辉三角定义如下：

#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 把每一行看做一个list，试写一个generator，不断输出下一行的list：

# 自己写的，测试失败；对于yield理解不够，不太明白
# def triangles():
#     L = []
#     a, b = 0, 0
#     NL = []
#     yield L
#     for i in L:
#         a, b = i, a
#         NL.append(a+b)

#     NL.append(1)
#     L = NL
#     yield L

# 评论区参考
# 灵活应用列表生成式 真的理解了这个数据的格式与算法，学习了！！

def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i+1] for i in range(len(L) - 1)] + [1]

# next(triangles())
# next(triangles())
# next(triangles())
# next(triangles())


# print(triangles())

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
