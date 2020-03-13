# -*- coding: utf-8 -*-

# 序列机基本操作
# 序列，定义一个序列，利用偏移量进行取值
zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

# print(zodiac[0])
# print(zodiac[0:4]) #切片操作符
# print(zodiac[-1])

# year = 2020
# print(year,'年的生肖为',zodiac[year%12])

# 判断成员关系
# print('虎' not in zodiac)
# print('虎' in zodiac)

# 连接操作 +
# print('十二生肖为：'+zodiac)
# print(zodiac[-1] + zodiac[0])

# 重复操作 *
print(zodiac*3)
print(zodiac+'\r\n'*3)
print((zodiac+'\r\n')*3)
print(zodiac[0]*3)