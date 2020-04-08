# -*- coding:utf-8 -*-
# t = (1,2)

# print(t)

# print(len(t))

# print(t[0])

# print(t[-1])

# t[0] = 9
# Traceback (most recent call last):
#   File ".\Exercise\08.tuple.py", line 12, in <module>
#     t[0] = 9
# TypeError: 'tuple' object does not support item assignment

# t1 = (1)

# print(t1) #()为小括号，结果为1

# t2 = (1,) # 只有一个元素增加一个逗号消除歧义

# print(t2)

# t = (1,2,[3,4])

# print(t)

# print(t[-1])

# t[-1][0] = 5 # tuple指向不变，元素值发生变化;利用list的可变性对tuple进行扩展

# print(t)

# t[-1].append(8)

# print(t)

# 练习

# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]

# print(L[0][0])

# print(L[1][1])

# print(L[-1][-1])

print(type(()))