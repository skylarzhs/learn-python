#!/usr/bin/env python3
# -*- coding : utf-8 -*-

from collections import OrderedDict

class LastUpdateOrderedDict(OrderedDict):
    def __init__(self,capacity):
        super(LastUpdateOrderedDict,self).__init__()
        self._capacity = capacity
    
    def __setitem__(self,key,value):

        containsKey = 1 if key in self else 0

        if len(self) - containsKey >= self._capacity:
            # 删除末尾键
            last = self.popitem(last=False)
            print('remove:',last)
        
        if containsKey:
            del self[key]
            print('set item:',(key,value))
        else:
            print('add item:',(key,value))
        
        OrderedDict.__setitem__(self,key,value)


lurd = LastUpdateOrderedDict(3)

lurd['a'] = 1
print(lurd)
lurd['b'] = 1
print(lurd)
lurd['c'] = 1
print(lurd)
lurd['a'] = 1
print(lurd)
lurd['d'] = 1
print(lurd)

# add item: ('a', 1)
# LastUpdateOrderedDict([('a', 1)])
# add item: ('b', 1)
# LastUpdateOrderedDict([('a', 1), ('b', 1)])
# add item: ('c', 1)
# LastUpdateOrderedDict([('a', 1), ('b', 1), ('c', 1)])
# set item: ('a', 1)
# LastUpdateOrderedDict([('b', 1), ('c', 1), ('a', 1)])
# remove: ('b', 1)
# add item: ('d', 1)
# LastUpdateOrderedDict([('c', 1), ('a', 1), ('d', 1)])

# a
# a b
# a b c
# b c a
# c a d
