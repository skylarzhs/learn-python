# -*- encoding : utf-8 -*-

# 生成[1x1, 2x2, 3x3, ..., 10x10]

# L = [x*x for x in range(1, 11)]

# print(L)

# L = [x*x for x in range(1, 11) if x%2 == 0]

# print(L)

# >>> [x*x for x in range(1,11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# >>> [x*x for x in range(1,10)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81]
# >>> [x*x for x in range(1,10) if x%2 == 0]
# [4, 16, 36, 64]
# >>> [m+n for m in 'ABC' for n in 'OPG'] # 两层循环
# ['AO', 'AP', 'AG', 'BO', 'BP', 'BG', 'CO', 'CP', 'CG']

# >>> import os
# >>> [d for d in os.listdir('.')]
# ['.git', 'Exercise', 'Tutorial', '.gitignore', 'README.md']
# >>> [d for d in os.listdir('D')]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# FileNotFoundError: [WinError 3] 系统找不到指定的路径。: 'D'
# >>> [d for d in os.listdir('D:')]
# ['$RECYCLE.BIN', 'backupdata']

# for 同时使用多个变量
# [x+'='+y for x,y in {'a':'1','b':'ppp'}.items()]

# 练习

# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：

L1 = ['Hello', 'World', 18, 'Apple', None]

# L2 = [l if not isinstance(l,str) else l.lower() for l in L1] # 只转换，不过滤
L2 = [l.lower() for l in L1 if isinstance(l, str)]  # 转换并过滤


# 测试:
print(L2)

if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
