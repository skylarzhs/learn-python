#!/usr/bin/env python3
# -*- coding : utf-8 -*-

from collections import ChainMap
import os
import argparse

# 构造缺省参数
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数

parser = argparse.ArgumentParser()
parser.add_argument('-u','--user')
parser.add_argument('-c','--color')
namespace = parser.parse_args()
command_line_args = {k:v for k,v in vars(namespace).items() if v}

# 组合成ChainMap
combined = ChainMap(command_line_args,os.environ,defaults)

print('color = %s' % combined['color'])
print('user = %s' % combined['user'])

# python .\Exercise\62.ChainMap.py
# color = red
# user = guest
# python .\Exercise\62.ChainMap.py -c blue
# color = blue
# user = guest
# python .\Exercise\62.ChainMap.py -c blue -uSkylar
# color = blue
# user = Skylar