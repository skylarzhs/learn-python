#!/usr/bin/env python3
# -*- coding : utf-8 -*-

from urllib.request import urlopen
from contextlib import closing
from contextlib import contextmanager


class Query(object):
    def __init__(self, name):
        self.name = name

    # def __enter__(self):
    #     print('enter')
    #     return self

    # def __exit__(self,exec_type,exec_value,traceback):
    #     if exec_type:
    #         print('Error')
    #     else:
    #         print('exit')

    def query(self):
        print('Query info about %s' % self.name)


@contextmanager
def create_query(name):
    print('begin')
    q = Query(name)
    yield q
    print('end')

# with Query('Bob') as q:
#     q.query()


with create_query('Bob') as q:
    q.query()


@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)


with tag('h1'):
    print('Hello')
    print('world')

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)