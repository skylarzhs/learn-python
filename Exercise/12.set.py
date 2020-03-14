# -*- encoding:utf-8 -*-

# s = set([1, 2, 3, 6, 4, 5, 2, 6])

# print(s)

# s.add(2)

# print(s)

# s.add(7)

# print(s)

# s.add(0)

# print(s)

# s.remove(2)

# print(s)

# s1 = set([2, 4, 9])

# print(s & s1) # 交集

# print(s | s1) # 并集

s = set([1,2.3])

# s.add([1,2,3])
# Traceback (most recent call last):
#   File ".\Exercise\12.set.py", line 31, in <module>
#     s.add([1,2,3])
# TypeError: unhashable type: 'list'

s.add((1,2))

print(s)