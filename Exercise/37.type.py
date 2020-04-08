#!/usr/bin/env python3
# -*- coding : utf-8 -*-

'A type test'

__author__ = 'Skylar Zheng'

# >>> def fn(self,name='world'):
# ...     print('Hello %s' % name)
# ...
# >>> Hello = type('Hello',(object,),dict(hello=fn))
# >>> Hello
# <class '__main__.Hello'>
# >>> type(Hello)
# <class 'type'>
# >>> h = Hello()
# >>> type(h)
# <class '__main__.Hello'>
# >>> h()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'Hello' object is not callable
# >>> h.hello()
# Hello world