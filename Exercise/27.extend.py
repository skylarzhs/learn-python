#!/usr/bin/env python3
# -*- encoding:utf8 -*-

'Extends test file'

__author__ = 'Skylar Zheng'


class Animal(object):
    def run(self):
        print('Running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Test(object):
    def run(self):
        print('A cute thing')
        
c = Cat()
# c.run()

d = Dog()
# d.run()

# print(isinstance(c,Animal))
# print(isinstance(c,Cat))
# print(isinstance(d,Animal))
# print(isinstance(d,Cat))
# print(isinstance(c,Dog))


def print_twice(animal):
    animal.run()
    animal.run()


print_twice(Animal())
print_twice(c)
print_twice(d)

print_twice(Test())

