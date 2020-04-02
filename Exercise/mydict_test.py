#!/usr/bin/env python3
# -*- encoding : utf-8 -*-

"MyDict Unit test"

__author__ = 'Skylar Zheng'

import unittest
from mydict import Dict


class DictTest(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertEqual(d['key'], 'value')
        self.assertTrue('key' in d)

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

# if __name__ == '__main__':
#     unittest.main()
