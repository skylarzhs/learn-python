#!/usr/bin/env python3
# -*- coding : utf-8 -*-

from urllib import request, parse
from html.parser import HTMLParser
import time


with open(r'E:\projects\learn-python\Exercise\medicine.txt', 'r', encoding='UTF-8') as file:
    mlist = file.read().split("\n")
    # print(mlist)


class TextParser(HTMLParser):
    L = []

    def handle_data(self, data):
        data = data.replace(r'\n', '').replace(r'\t', '').replace(r'\s{4}', '')
        if data:
            self.L.append(data)


data = [
    ('t', '你是谁'),
    ('d', 1),
    ('s', None),
    ('k', 1),
    ('b', None),
    ('h', None),
    ('u', None),
    ('v', None),
    ('y', None),
    ('z', None),
    ('f', None),
    ('p', None),
    ('g', None),
    ('q', None),
    ('r', None),
    ('j', None),
    ('x', None),
    ('u_', None),
    ('p_', 1),
    ('tzg', None),
    ('tzgzt', 2),
    ('sxsg', None),
    ('sxsgxx', 1),
    ('f_', None),
    ('token', 'd6e092ae62734f7cb617c43c925ed7d1'),
]

for medicine in mlist:
    print('start deal medicine : %s' % medicine)
    data[0] = ('t', medicine)
    login_data = parse.urlencode(data)

    req = request.Request('https://www.qqxiuzi.cn/zh/pinyin/show.php')
    req.add_header('Host', 'www.qqxiuzi.cn')
    req.add_header('Origin', 'https://www.qqxiuzi.cn')
    req.add_header('Referer', 'https://www.qqxiuzi.cn/zh/pinyin/')
    req.add_header(
        'User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36')
    req.add_header('Content-type', 'application/x-www-form-urlencoded')
    req.add_header('Cookie', 'qqxiuzi_pinyin=0%2C1%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C1%2C0%2C2%2C0%2C1%2C1%2C0; PHPSESSID=ob4sf3hfg8otql5qc53sfdmp95; Hm_lvt_899df2cdf7f5a83a719fb1bb96982b18=1591407718; Hm_lpvt_899df2cdf7f5a83a719fb1bb96982b18=1591407718')

    py = ''

    with request.urlopen(req, data=login_data.encode('utf-8')) as f:
        print('Status:', f.status, f.reason)
        # print('Data', f.read().decode('utf-8'))
        html = f.read().decode('utf-8')
        parser = TextParser()
        parser.L = []
        parser.feed(html)
        # print(parser.L)
        s = ''.join(parser.L).split()
        py = ''.join([i[0] for i in s])
        print(py)

    with open(r'E:\projects\learn-python\Exercise\pinyin.txt', 'a', encoding='UTF-8') as file:
        file.write(medicine + "\t" + py+"\r")

    time.sleep(1)

