#!/usr/bin/env python3
# -*- coding:utf8 -*-

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

        
c = Cat()
d = Dog()

print(type(c))
print(type(d))
print(type(Animal))
print(type((Animal())))

def fn():
    pass

print(type(fn))

import types

print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)