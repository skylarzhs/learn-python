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

def person(name, age, **other):
    print('name:', name, 'age:', age, 'other', other)


person('Lisa', 12)
person('Tom', 21, city='JN')
person('Lisa', 12, city='LW', job='Engineer')


info = {'job':'PHPer','city':'BJ','sex':'F'}

person('Jane',32,**info)