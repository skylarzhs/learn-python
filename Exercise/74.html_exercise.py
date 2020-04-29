#!/usr/bin/env python3
# -*- coding : utf-8 -*-

from html.parser import HTMLParser
from urllib import request
import re


class MyEventsParser(HTMLParser):

    L = []
    i = 0
    record = 0
    n = 0
    t = 0
    y = 0
    addr = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'ul' and attrs[0][1] == 'list-recent-events menu':
            self.record = 1
        elif tag == 'li' and self.record == 1:
            self.L.insert(self.i, dict())
        elif tag == 'a' and self.record == 1:
            self.n = 1
        elif tag == 'time' and self.record == 1:
            self.t = 1
        elif tag == 'span' and self.record == 1 and attrs[0][1] == 'say-no-more':
            self.y = 1
        elif tag == 'span' and self.record == 1:
            self.addr = 1

    def handle_endtag(self, tag):
        if tag == 'ul' and self.record == 1:
            self.record = 0
        elif tag == 'li' and self.record == 1:
            self.i = self.i + 1
            # 储存值
        elif tag == 'a' and self.record == 1:
            self.n = 0
        elif tag == 'span' and self.record == 1:
            self.addr = 0
        elif tag == 'time' and self.record == 1:
            self.t = 0
            self.y = 0

    def handle_data(self, data):
        data = data.replace(r'\n', '').replace(r'\t', '').replace(r'\s{4}', '')
        if data:
            if self.n == 1:
                self.L[self.i]['name'] = data
            elif self.addr == 1:
                self.L[self.i]['addr'] = data
            elif self.y == 1:
                self.L[self.i]['t'] = self.L[self.i]['t'] +  data
            elif self.t == 1:
                self.L[self.i]['t'] = data


parser = MyEventsParser()
# with request.urlopen('https://www.python.org/events/python-events/') as f: # 网页无法打开，采用保存HTML度本地文件的形式
with open(r'E:\projects\learn-python\Tutorial\static\html\events.html', 'r') as f:
    html = f.read()


parser = MyEventsParser()
parser.feed(html)

for event in parser.L:
    print('会议名称：%s\t召开时间：%s\t召开地点：%s' % (event['name'],event['t'],event['addr']))
