#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import contextlib

class Query(object):
    def __init__(self,name):
        self.name = name
    
    def __enter__(self):
        print('enter')
        return self
    
    def __exit__(self,exec_type,exec_value,traceback):
        if exec_type:
            print('Error')
        else:
            print('exit')

    def query(self):
        print('Query info about %s' % self.name)



with Query('Bob') as q:
    q.query()

