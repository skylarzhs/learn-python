# -*- coding : utf-8 -*-

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

# from functools import reduce

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

# d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
#      '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


# def str2float(string):
#     dot_index = string.find('.')

#     str1 = string[:dot_index]
#     str2 = string[dot_index+1:]

#     def f1(x, y):
#         return 10 * x + y

#     def f2(x, y):
#         return 0.1 * x + y

#     def char2int(c):
#         return d[c]

#     return reduce(f1, map(char2int, str1)) + 0.1 * reduce(f2, map(char2int, reversed(str2)))


# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')

# filter

# 在一个list中，删掉偶数，只保留奇数

# def is_odd(x):
#     return x % 2 == 1

# print(list(filter(is_odd,[1.2,3,4,5,6,7,8,9])))

# 把一个序列中的空字符串删掉

# def is_blank(s):
#     return s != ' '

# print(list(filter(is_blank,'He l  lo, world !')))

# 求素数  埃氏筛法
# （1）先把1删除（现今数学界1既不是质数也不是合数）
# （2）读取队列中当前最小的数2，然后把2的倍数删去
# （3）读取队列中当前最小的数3，然后把3的倍数删去
# （4）读取队列中当前最小的数5，然后把5的倍数删去
# （5）读取队列中当前最小的数7，然后把7的倍数删去
# （6）如上所述直到需求的范围内所有的数均删除或读取

# 定义从3开始的奇数列

# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n

# 定义筛选函数


# def _not_divisible(n):
#     return lambda x: x % n > 0

# 定义生成器，不断返回下一个素数

# def primes():
#     n = 2
#     yield n
#     it = _odd_iter()

#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible(n), it)


# n = 0

# d = primes()
# for i in d:
#     if n < 100:
#         print(i)
#     else:
#         break

#     n = n+1

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数

# def is_palindrome(num):
#     num = str(num)
#     p = (len(num) + 1)//2
#     n = 0

#     ret = True

#     while n < p:
#         if num[n] != num[-n-1]:
#             return False
#         n = n + 1
#     return ret


# 灵活运用切片 !!!!!!
def is_palindrome(num):
    return str(num) == str(num)[::-1]


# print(is_palindrome(11221))

# L = [1122,4455,4554,1221,12345]

# print(list(filter(is_palindrome,L)))

# 测试:
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')

# sorted

# print(sorted([1, 4, 6, 2, 3, 1]))

# print(sorted([1, 5, -9, 8, -2]))

# print(sorted([1, 5, -9, 8, -2], key=abs))

# print(sorted([1, 5, -9, 8, -2], reverse=True))

# print(sorted([1, 5, -9, 8, -2], key=abs, reverse=True))

# print(sorted(['bob', 'about', 'Zoo', 'Credit']))

# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

# 练习
# 假设我们用一组tuple表示学生名字和成绩：

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0].lower()


L2 = sorted(L, key=by_name)

print(L2)


def by_score(t):
    return t[1]


L3 = sorted(L, key=by_score, reverse=True)

print(L3)
