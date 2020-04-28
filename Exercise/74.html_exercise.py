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
    addr = 0

    def handle_starttag(self, tag, attrs):
        # print(attrs)
        if tag == 'ul' and 'class' in attrs and attrs[0][1] == 'list-recent-events':
            print('ul start')
            self.record = 1
        elif tag == 'li' and self.record == 1:
            self.L[self.i] = dict()
        elif tag == 'a' and self.record == 1:
            self.n = 1
        elif tag == 'time' and self.record == 1:
            self.L[self.i]['time'] = attrs['datetime']
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

    def handle_data(self, data):
        data = data.replace(r'\n', '')
        if data:
            if self.n == 1:
                self.L[self.i]['name'] = data
            elif self.addr == 1:
                self.L[self.i]['addr'] = data


parser = MyEventsParser()
# with request.urlopen('https://www.python.org/events/python-events/') as f:
with open(r'E:\projects\learn-python\Tutorial\static\html\events.html', 'r') as f:
    html = f.read().replace(r'\n', '')
    # content = re.match(r'<ul class="list-recent-events menu">.+?<ul>', html)
    # print(content)


parser = MyEventsParser()
parser.feed(html)

print(parser.L)
