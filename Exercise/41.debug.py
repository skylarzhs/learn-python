#!/usr/bin/env python3
# -*- coding : utf-8 -*-

# import logging
# logging.basicConfig(level=logging.DEBUG)

def foo(s):
    n = int(s)
    # logging.debug('n = %s' % n)
    # assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

main()