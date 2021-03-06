#!/usr/bin/env python3
# -*- coding : utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print('<%s>' % tag)
    
    def handle_endtag(self,tag):
        print('</%s>' % tag)
    
    def handle_startendtag(self,tag):
        print('<%s/>' % tag)
    
    def handle_data(self,data):
        print(data.replace(' ','.').replace('\n',r'\n'))
    
    def handle_comment(self,data):
        print('<!--',data,'-->')
    
    def handle_entityref(self,name):
        print('&%s' % name)
    
    def handle_charref(self,name):
        print('&#%s' % name)
    

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

# feed可以多次调用

# <html>


# <head>
# </head>


# <body>


# <!--  test html parser  -->


# <p>
# Some
# <a>
# html
# </a>
#  HTML tutorial...
# <br>
# END
# </p>


# </body>
# </html>

# <html>
# \n
# <head>
# </head>
# \n
# <body>
# \n
# <!--  test html parser  -->
# \n....
# <p>
# Some.
# <a>
# html
# </a>
# .HTML tutorial...
# <br>
# END
# </p>
# \n
# </body>
# </html>