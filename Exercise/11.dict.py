# -*- encoding:utf-8 -*-

d = {'Tom': 78, 'Jane': 88, 'Pony': 67}

print(d)

# print(d['Tom'])

# d['Tom'] = 77

# print(d)

# print(d['Skylar']) # KeyError

# print('Skylar' in d) # 判断key是否存在

# print(d.get('Tom')) 
# print(d.get('Skylar')) # None
# print(d.get('Skylar','100')) #设置默认值，只是显示打印用，不会增加元素

# print(d)


# 删除 pop

# d.pop('Tom')

# print(d)

d['Alisa'] = 87

print(d)

# d[[1,2]] = 22 ERROR
# Traceback (most recent call last):
#   File ".\Exercise\11.dict.py", line 34, in <module>
#     d[[1,2]] = 22
# TypeError: unhashable type: 'list'

# d[(1,2)] = 22 #tuple 为不变对象

# d[(1,2,[3,4])] = 99 #ERROR
# Traceback (most recent call last):
#   File ".\Exercise\11.dict.py", line 42, in <module>
#     d[(1,2,[3,4])] = 99
# TypeError: unhashable type: 'list'
