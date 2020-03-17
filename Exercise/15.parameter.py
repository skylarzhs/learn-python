# -*- encoding:utf-8 -*-

# 计算某值的平方
# def power(x):
#     return x*x

# print(power(5))

# 计算某数的n次方


# def power(x, n = 2):
#     if not isinstance(x, (int, float)):
#         raise('Type error')
#     if not isinstance(n, (int,)):
#         raise('Type error')

#     s = 1

#     while n > 0:
#         s = s * x
#         n = n - 1
#     return s


# x = input('Pleaser enter a number as the base:\r\n')

# n = input('Please enter a number as a multiplier\r\n')

# n = int(n)
# x = int(x)

# print('The result is %d' % power(x, n))

# 默认参数

# def enroll(name, gender, age = 18, city = 'JN'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)

# enroll('Skylar','F',23,'JN')

# enroll('Skylar','F')

# enroll('Jane','M',22,'LW')

# enroll('Tom','F',city='TA')

# 默认参数的坑

# def add_end(L=[]):
#     L.append('END')
#     return L

# print(add_end([1,2,3]))
# print(add_end([1,2,3]))
# print(add_end(['x','y']))

# print(add_end())
# print(add_end())
# print(add_end())

# 函数在定义的时候，默认参数L的值就被计算出来，即[]，因为默认参数L也是一个变量，他指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

# 利用 None 对象修改

# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L

# print(add_end())
# print(add_end())
# print(add_end())

# 给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……

# def calc(numbers):
#     s = 0
#     for i in numbers:
#         s = s + i*i

#     return s

# print(calc([1,2,3]))

# 可变参数修改，增加*，函数内部默认接收一个tuple

# def calc(*numbers):
#     s = 0
#     for i in numbers:
#         s = s + i * i
#     return s

# print(calc(1,2,3)) #可变参数调用

# print(calc()) # 无参数

# l = [2,3,4]

# print(calc(*l)) #使用可变参数方式，调用已有list

# 关键字参数

# def person(name, age, **other):
#     print('name:', name, 'age:', age, 'other', other)


# person('Lisa', 12)
# person('Tom', 21, city='JN')
# person('Lisa', 12, city='LW', job='Engineer')


# info = {'job':'PHPer','city':'BJ','sex':'F'}

# person('Jane',32,**info)

# 命名关键字参数

# def person(name, age, *, city, job):
#     print(name, age, city, job)


# person('A', 12, city='SD', job='Eng')

# person('B', 12, job='Eng',city='JN') # 与位置无关

# person('C', 12) # ERROR

# Traceback (most recent call last):
#   File ".\Exercise\15.parameter.py", line 131, in <module>
#     person('C', 12)
# TypeError: person() missing 2 required keyword-only arguments: 'city' and 'job'

# person('B', 12, 'Eng', 'JN') #ERROR 命名关键字必须传入变量名
# Traceback (most recent call last):
#   File ".\Exercise\15.parameter.py", line 138, in <module>
#     person('B', 12, 'Eng', 'JN')
# TypeError: person() takes 2 positional arguments but 4 were given

# 函数中已经有一个可变参数，后面的命名关键字参数不再需要一个特殊分隔符`*`

# def person(name, age, *args, city, job='Teacher'):
#     print(name, age, args, city, job)


# person('D', 12, 999,'AAAAA', city='BJ')

# 关键字参数兼容可变参数，不兼容关键字参数。
# def person(name, age, **args, city, job='Teacher'):
#     print(name, age, args, city, job)


# person('D',sex='F', year='2020', city='BJ')

# PS F:\projects\learn-python> python .\Exercise\15.parameter.py
#   File ".\Exercise\15.parameter.py", line 153
#     def person(name, age, **args, city, job='Teacher'):
#                                   ^
# SyntaxError: invalid syntax

# 参数组合

# def func1(a, b=0, *c, **d):
#     print(a, b, c, d)


# func1(1, 2, 3, 4, 5)

# func1(6, 999, 'ppp',e=444, f=888)

# def f1(a, b, c=0, *args, **kw):
#     print(a, b, c, args, kw)


# def f2(a, b, c=0, *, d, **kw):
#     print(a, b, c, d, kw)


# f1(1, 2)

# f1(1, 2, 3)

# f1(1, 2, 3, 4, 5)

# f1(1, 2, 3, 4, 5, cc=9, m='p')

# f2(1,2,3,d=999)

# f2(2,3,4,d=898,dd='opq')

# list tuple

# args = (1, 2, 3, 4)

# kw = {'kw1': 1122, 'kw2': 990}

# f1(*args, *kw) #单个*取键名作为可变参数的一部分
# # 1 2 3 (4, 'kw1', 'kw2') {}

# f1(*args, **kw)
# # 1 2 3 (4,) {'kw1': 1122, 'kw2': 990}


# 练习题目

# def product(x, y):
#     return x*y

def product(x, *nums):
    if not isinstance(x, (int, float)):
        raise TypeError('Type ERROR')
    m = x
    for i in nums:
        if not isinstance(i, (int, float)):
            raise TypeError('Type ERROR')
        m = m * i
    return m


# print(product(1))
# print(product(1, 2))
# print(product(1, 2, 3))
# print(product(1, 2, 3, 4))

# print(product(1, 'p'))

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
