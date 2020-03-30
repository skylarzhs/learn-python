#!/usr/bin/env python3
# -*- encoding : utf-8 -*-

# metaclass是类的模板，所以必须从`type`类型派生：


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list,metaclass = ListMetaclass):
    pass

#当传入metaclass关键字的时候，魔术就生效了，它指示Python解释器在创建MyList时，要通过`ListMetaclass.__new__()`来创建，在此，我们可以修改类的定义。

L = MyList()

L.add(1)

print(L)