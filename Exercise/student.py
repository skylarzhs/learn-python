#!/usr/bin/env python3
# -*- encoding : utf-8 -*-

'A class test'

__author__ = 'Skylar Zheng'


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_info(self):
        print('name：%s score: %s' % (self.name,self.score))

    def get_grade(self):
        if self.score <= 60:
            return 'C'
        elif self.score <= 80:
            return 'B'
        else:
            return 'A'

