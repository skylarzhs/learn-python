#!/usr/bin/env python3
# -*- coding : utf-8 -*-

'Class attribute test'

__author__ = 'Skylar Zheng'

class Student(object):
    count = 0

    def __init__(self,name):
        self.name = name
        Student.count = Student.count + 1

# s1 = Student('Jane')

# print(s1.count)

# print(Student.count)

# s2 = Student('Skylar')

# print(s2.count)

# print(Student.count)


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')