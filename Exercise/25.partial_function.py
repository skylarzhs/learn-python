# -*- encoding : utf-8 -*-

import functools

int2 = functools.partial(int,base=2)

x = int2('10')

print(x)