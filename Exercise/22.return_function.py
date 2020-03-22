# -*- encoding:utf-8 -*-

# 可变参数求和

# def calc_sum(*args):
#     ax = 0
#     for i in args:
#         ax = ax + i
#     return ax

# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for i in args:
#             ax = ax + i
#         return ax
#     return sum

# print(calc_sum(1,2,3,4,5))

# f = lazy_sum(1,2,3,4,5)

# print(f)

# print(f())

# 闭包


# def count():
#     fs = []
#     for i in range(1, 4):
#         # print(i)
#         def f():
#             return i * i
#         # print(f)
#         fs.append(f)
#         # print(fs)
#     return fs


# f1, f2, f3 = count()

# print(11111111111)
# print(f1())
# print(2222222222222)

# print(f2())
# print(3333333333333)

# print(f3())

# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。


# 1
# <function count.<locals>.f at 0x000002D93D70E280>
# [<function count.<locals>.f at 0x000002D93D70E280>]
# 2
# <function count.<locals>.f at 0x000002D93D70E310>
# [<function count.<locals>.f at 0x000002D93D70E280>, <function count.<locals>.f at 0x000002D93D70E310>]
# 3
# <function count.<locals>.f at 0x000002D93D70E3A0>
# [<function count.<locals>.f at 0x000002D93D70E280>, <function count.<locals>.f at 0x000002D93D70E310>, <function count.<locals>.f at 0x000002D93D70E3A0>]
# 11111111111
# 9
# 2222222222222
# 9
# 3333333333333
# 9

# def count():
#     def f(j):
#         def g():
#             return j * j
#         return g

#     fs = []
#     for i in range(1, 4):
#         print(fs)
#         print(i)
#         print(f(i))
#         fs.append(f(i))
#         print(9999999)
#     print(fs)
#     return fs


# f1, f2, f3 = count()


# print(111111)
# print(f1)

# print(f2)

# print(f3)


# print(f1())

# print(f2())

# print(f3())

# PS python .\Exercise\22.return_function.py
# []
# 1
# <function count.<locals>.f.<locals>.g at 0x000001E53793E310>
# 9999999
# [<function count.<locals>.f.<locals>.g at 0x000001E53793E310>]
# 2
# <function count.<locals>.f.<locals>.g at 0x000001E53793E3A0>
# 9999999
# [<function count.<locals>.f.<locals>.g at 0x000001E53793E310>, <function count.<locals>.f.<locals>.g at 0x000001E53793E3A0>]
# 3
# <function count.<locals>.f.<locals>.g at 0x000001E53793E430>
# 9999999
# [<function count.<locals>.f.<locals>.g at 0x000001E53793E310>, <function count.<locals>.f.<locals>.g at 0x000001E53793E3A0>, <function count.<locals>.f.<locals>.g at
# 0x000001E53793E430>]
# 111111
# 1
# 4
# 9

# lambda 缩减代码

# def count():
#     def f(j):
#         return lambda : j * j

#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i))
        
#     return fs

# f1, f2, f3 = count()

# print(f1())

# print(f2())

# print(f3())

# 练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：

def createCounter():
    def counter(i):
        return  i + 1
    
    L = []
    i = 0
    while True:
        it = counter(i)
        L.append(it)
        i = i + 1
    return L

f1 = createCounter()

print(f1)

# print(f1(),f1(),f1())