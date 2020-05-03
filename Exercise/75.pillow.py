#!/usr/bin/env python3
# -*- coding : utf-8 -*-

from PIL import Image, ImageFilter, ImageDraw, ImageFont

# im = Image.open(r'E:\projects\learn-python\Tutorial\static\image\64.png')

# 缩放
# w, h = im.size

# print('Original image size:%s x %s' % (w, h))

# im.thumbnail((w//2, h//2))

# im.save(r'E:\projects\learn-python\Tutorial\static\image\64_2.png')

# 模糊

# im2 = im.filter(ImageFilter.BLUR)

# im.save(r'E:\projects\learn-python\Tutorial\static\image\64_blur.png')

# 生成验证码

import random


def rndChr():
    return chr(random.randint(65, 90))


def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


width = 240
height = 60

image = Image.new('RGB', (width, height), (255, 255, 255))

font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 36)

draw = ImageDraw.Draw(image)

for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

for t in range(4):
    draw.text((60*t+10, 10), rndChr(), font=font, fill=rndColor2())

image = image.filter(ImageFilter.BLUR)

image.save('verify.jpg', 'jpeg')
