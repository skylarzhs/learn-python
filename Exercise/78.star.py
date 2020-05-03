#!/usr/bin/env python3
# -*- coding : utf-8 -*-

from turtle import *

# 设置笔刷宽度:
def drawStar(x,y):
    pu()
    goto(x,y)
    pd()
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)

for x in range(0,255,50):
    drawStar(x,0)

done()