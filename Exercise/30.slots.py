#! /usr/bin/env python3
# -*- encoding : utf-8 -*-

from types import MethodType
'__slots__ test'

__author__ = 'Skylar Zheng'


class Student(object):
    # __slots__ = ('name','age')
    pass


s1 = Student()

s1.name = 'Jane'

print(s1.name)

s1.age = 34

print(s1.age)

s1.score = 87

print(s1.score)


def set_score(self, score):
    self.score = score


s1.set_score = MethodType(set_score, s1)

s1.set_score(129)

print(s1.score)


# class GraduateStudent(Student):
#     pass

# s2 = GraduateStudent()

# s2.name = 'Skylar'

# print(s2.name)

# s2.age = 12

# print(s2.age)

# s2.score = 99

# print(s2.score)
