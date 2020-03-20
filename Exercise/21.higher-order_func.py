# -*- encoding : utf-8 -*-

# 高阶函数

# def add(a,b,f):
#     return f(a) + f(b)

# print(add(-1,78,abs))

# print(add(-5, 6, abs))

# map
# L = [1,2,3,4,5,6,7,8,9]


# def f(x):
#     return x*x

# m = map(f,L)

# print(m)

# for i in m:
#     print(i)

# print(list(m))

# L = list(map(str,[1,2,3,4,5,6,7,8,9]))

# print(L)

# reduce

# from functools import reduce
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)


# def f(a, b):
#     return a+b


# r = reduce(f, [1, 2, 3, 4, 5])

# print(r)

# 数字字符串转换成int，并进行计算

# def f(c):
#     d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
#          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return d[c]


# def add(x, y):
#     return 10 * x + y


# # 两个函数的结合
# print(reduce(add, map(f, '123456')))

# str2int函数

# def str2int(str):
#     from functools import reduce

#     def char2num(c):
#         d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
#              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#         return d[c]

#     def f(x, y):
#         return x * 10 + y

#     return reduce(f,map(char2num,str))


# 优化
# import 语句提前
# 转换字典定义提前

from functools import reduce

# d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
#      '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


# def str2int(str):

#     def char2num(c):
#         return d[c]

#     def f(x, y):
#         return x * 10 + y

#     return reduce(f, map(char2num, str))


# print('123456')

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

# d1 = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M',
#       'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}

# d2 = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm',
#       'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'}

# 构建字典

# def formatName(name):
#     i = 0
#     new_name = ''
#     for c in name:
#         if i == 0:
#             if ord(c) > ord('Z'):
#                 c = d1[c]
#         else:
#             if ord(c) < ord('a'):
#                 c = d2[c]
#         i = i + 1
#         new_name = new_name + c
#     return new_name

# 利用函数

# def formatName(name):
#     i = 0
#     new_name = ''
#     for c in name:
#         if i == 0:
#             if ord(c) > ord('Z'):
#                 c = c.upper()
#         else:
#             if ord(c) < ord('a'):
#                 c = c.lower()
#         i = i + 1
#         new_name = new_name + c
#     return new_name


# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(formatName, L1))
# print(L2)

# 练习2：Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

# def prod(L):

#     def multiply(x,y):
#         return x * y
#     return reduce(multiply,L)

# 测试

# print(prod([1,2,3,4]))

# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

# 练习3：利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
     '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2float(string):
    dot_index = string.find('.')

    str1 = string[:dot_index]
    str2 = string[dot_index+1:]

    def f1(x, y):
        return 10 * x + y

    def f2(x, y):
        return 0.1 * x + y

    def char2int(c):
        return d[c]

    return reduce(f1, map(char2int, str1)) + 0.1 * reduce(f2, map(char2int, reversed(str2)))


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
