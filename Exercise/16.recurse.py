# -*- coding : utf-8 -*-

# 计算某值的阶乘

# 递归函数：调用自身，处理临界值
# def fact(n):
#     if not isinstance(n, (int,)):
#         raise TypeError('Please enter a int number')
#     if n < 1:
#         raise TypeError('type error')
#     if n > 1:
#         m = n * fact(n-1)
#     else:
#         m = 1

#     return m

# 尾递归修改

# print(fact(1))
# print(fact(2))
# print(fact(3))
# print(fact(4))
# print(fact(5))

# print(fact(1000)) #栈溢出
# RecursionError: maximum recursion depth exceeded in comparison


# def fact(n):
#     return fact_iter(n, 1)


# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num-1, num*product) # 计算结果

# print(fact(1000)) #栈溢出，结果看还是有栈溢出，python解析器没有做此优化

# 练习，汉诺塔的移动 
# H(1) = 1
# H(n) = 2H(n-1) + 1(n>1)
