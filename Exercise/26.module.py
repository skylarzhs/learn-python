#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

'A test module'

__author__ = 'Skylar Zheng'

import sys


def test():
    args = sys.argv
    if(len(args) == 1):
        print('Hello world !')
    elif(len(args) == 2):
        print('Hello %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()