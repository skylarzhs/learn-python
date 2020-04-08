#!/usr/bin/env python3
# -*- coding : utf-8 -*-


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    # def users(self, name):
    #     return Chain('%s/users/%s' % (self._path, name))

    def __call__(self, name):
        return Chain('%s/%s' % (self._path, name))

# print(Chain().api.doctor)


# print(Chain()())
p = Chain().users('michael').repos

print(p)
