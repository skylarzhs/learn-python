# -*- coding:utf-8 -*-

# L = ['A','B','C','D','E','F']

# # 取前3个元素

# print(L[0:3])

# print(L[:3])

# print(L[-1:])

# print(L[-3:-1])

# 定义一个函数，实现trim()函数，去除字符串首尾的空格。

# def trim(s):
#     l = len(s)
#     if l % 2 == 0:
#         l = l/2
#     else:
#         l = (l+1)/2
#     i = 0
#     while i < l:
#         if s[0] == ' ':
#             s = s[1:]
#         if len(s) > 0 and s[-1] == ' ':
#             s = s[:-1]
#         i = i + 1

#     return s

# 参考解法，简洁扼要，避免了''报错问题，赞！！！

def trim(s):
    while s[-1:] == ' ':
        s = s[:-1]
    while s[:1] == ' ':
        s = s[1:]
    return s

# 测试


if trim('hello ') != 'hello':
    print('Failed！')
elif trim(' hello') != 'hello':
    print('Failed！')
elif trim(' hello ') != 'hello':
    print('Failed！')
elif trim(' hello world ') != 'hello world':
    print('Failed！')
elif trim('') != '':
    print('Failed！')
elif trim('  ') != '':
    print('Failed！')
elif trim('   ') != '':
    print('Failed！')
elif trim('    ') != '':
    print('Failed！')
else:
    print('Well done!')
