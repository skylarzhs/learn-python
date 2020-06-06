#!/usr/bin/env python3
# -*- coding : utf-8 -*-

from pypinyin import pinyin

# print(pinyin(u'阿胶粉(代)', style=4))


with open(r'E:\projects\learn-python\Exercise\medicine.txt', 'r', encoding='UTF-8') as file:
    mlist = file.read().split("\n")


for m in mlist:
    l = pinyin(m, style=4)
    py = ''.join([i[0] for i in l])
    with open(r'E:\projects\learn-python\Exercise\pinyin.txt', 'a', encoding='UTF-8') as file:
        file.write(py+"\r")
