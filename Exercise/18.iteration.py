# -*- encoding:utf-8 -*-

# d = {'f':89,'a':123,'b':234,'c':345}

# print(d)

# # 默认迭代key值
# for key in d:
#     print(key)

# # 迭代value
# for v in d.values():
#     print(v)

# # 迭代 k v
# for k,v in d.items():
#     print('k = ',k,'v = ',v)

# str

# s = 'ASDF'

# for i in s:
#     print(i)

# L = [1,2,3,'H','P']

# for i,v in enumerate(L):
#     print(i,v)

# t = ((1,2),(3,4),(5,6))

# for x,y in t:
#     print(x,y)

# 练习，使用迭代查找一个list中的最大和最小值，并返回一个tuple

# 在此练习中没有考虑 None 的情况，按照正序流程

def findMinAndMax(L):

    if len(L) == 0:
        return (None,None)

    min = L[0]
    max = L[0]
    
    for v in L:
        if v > max:
            max = v
        if v < min:
            min = v
    return min, max


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
