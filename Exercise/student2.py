#!/usr/bin/env python3
# -*- coding : utf-8 -*-

'Access Control'

__author__ = 'Skylar Zheng'


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_info(self):
        print('name：%s score: %s' % (self.__name, self.__score))

    def get_grade(self):
        if not isinstance(self.__score,(int,float)):
            raise ValueError('score is not invalid')
        if self.__score > 100 or self.__score < 0:
            raise ValueError('score is not invalid')
        if self.__score < 60:
            return 'C'
        elif self.__score < 80:
            return 'B'
        else:
            return 'A'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name
        return True

    def set_score(self, score):
        if score >100 or score <0:
            raise ValueError('Value Error')
        self.__score = score
        return True
