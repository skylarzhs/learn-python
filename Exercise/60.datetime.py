#!/usr/bin/env python3
# -*- coding : utf-8 -*-

from datetime import datetime

# now = datetime.now()

# print(now)

# print(type(now))

# 2020-04-14 16:36:08.139230
# <class 'datetime.datetime'>

# dt = datetime(2020,4,15,2,30,23,78)

# print(dt)

# dt = datetime.now()

# ts = dt.timestamp()

# print(ts)

# print(datetime.fromtimestamp(ts))

# print(datetime.utcfromtimestamp(ts))

# 2020-04-14 16:44:40.645941
# <class 'datetime.datetime'>
# 2020-04-15 02:30:23.000078
# 1586853880.646939
# 2020-04-14 16:44:40.646939
# 2020-04-14 08:44:40.646939

now = datetime.now()

print(now.strftime('%a , %b %d %H:%M'))