# -*- encoding:utf-8 -*-

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 将每个元素带入变量i，执行语句块中的语句
# sum = 0
# for i in list1:
#     # print(i)
#     sum = sum + i

# print(sum)

# test1 = list(range(100)) #range函数可以生成整数序列，可以转化为列表

# print(test1)

# sum = 0

# for j in test1:
# for j in range(101):
#     sum = sum+j

# print(sum)

# 计算100以内的奇数和

# sum = 0
# i = 1

# while i < 100:
#     sum = sum+i
#     i = i+2

# print(sum)
# print(i)

# 请利用循环依次对list中的每个名字打印出Hello, xxx!：

# L = ['Bart', 'Lisa', 'Adam']

# for name in L:
#     if name == 'Lisa':
#         # break
#         continue
#     print('Hello,%s!' % name)

# 重要提醒！！！
# 不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。

# 死循环

# while True:
#     print('True')