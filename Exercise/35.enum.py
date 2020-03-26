#!/usr/bin/env python3
# -*- encoding : utf-8 -*-

from enum import Enum, unique


# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May',
#                        'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# for name, member in Month.__members__.items():
#     print('%s => %s' % (name, member.value))

# value属性则是自动赋给成员的int常量，默认从1开始计数。

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sta = 6

print(Weekday.Sun)
print(Weekday['Sun'])
print(Weekday.Sun.value)
print(Weekday(1))
