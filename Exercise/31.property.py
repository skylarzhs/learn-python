#! /usr/bin/env python3
# -*- encoding : utf-8 -*-

'@property test'

__author__ = 'Skylar Zheng'


# class Student(object):

#     @property
#     def birth(self):
#         return self.__birth

#     @birth.setter
#     def birth(self, birth):
#         self.__birth = birth

#     @property
#     def age(self):
#         return 2020 - self.__birth


# s = Student()

# print(s)

# s.birth = 2000

# print(s.birth)

# print(s.age)

class Screen(object):
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise('Please enter a integer!')
        elif width < 0:
            raise('Please enter a integer gt 0')
        self.__width = width
        return True

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise('Please enter a integer!')
        elif height < 0:
            raise('Please enter a integer gt 0')
        self.__height = height
        return True

    @property
    def resolution(self):
        return self.__width * self.__height


s = Screen()

s.height = 100

s.width = 200

print(s.width)
print(s.height)

print(s.resolution)

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
