#!/usr/bin/env python3
# -*- coding : utf-8 -*-

from html.parser import HTMLParser
from urllib import request
import re

L = []
i = 0
n = 0
t = 0
d = 0
addr = 0


class MyEventsParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        print(data)


parser = MyEventsParser()
# with request.urlopen('https://www.python.org/events/python-events/') as f:
with open(r'E:\projects\learn-python\Tutorial\static\html\events.html', 'r') as f:
    html = f.read().replace('\n', '').replace('&nbsp;', '')
    # print(html)
    content = re.match(r'\<ul class="list-recent-events menu"\>', html)
    print(content)
