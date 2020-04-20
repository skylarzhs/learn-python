#!/usr/bin/env python3
# -*- coding : utf-8 -*-

from urllib import request

# with request.urlopen('https://yesno.wtf/api') as f:
#     data = f.read()
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s' % (k,v))
#     print("data:",data.decode('utf-8'))

# Status: 200 OK
# Content-Type:application/json; charset=utf-8
# Transfer-Encoding:chunked
# Connection:close
# Status:200 OK
# Cache-Control:max-age=0, private, must-revalidate
# Access-Control-Allow-Origin:*
# X-XSS-Protection:1; mode=block
# X-Request-Id:29b5d69e-4817-49c2-a6df-de09ccb59863
# ETag:"695a36fc9e094543e9927627178307e3"
# X-Frame-Options:SAMEORIGIN
# X-Runtime:0.002699
# X-Content-Type-Options:nosniff
# Access-Control-Request-Method:*
# Date:Mon, 20 Apr 2020 13:27:11 GMT
# X-Powered-By:Phusion Passenger 6.0.4
# Server:nginx/1.17.3 + Phusion Passenger 6.0.4
# data: {"answer":"no","forced":false,"image":"https://yesno.wtf/assets/no/12-dafd576be23d3768641340f76658ddfe.gif"}

# 发送请求
# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent','Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

# with request.urlopen(req) as f:
#     data = f.read()
#     # print(data)
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s' % (k,v))
#     print("data:",data.decode('utf-8'))

import json
# 利用urllib读取JSON，然后将JSON解析为Python对象
def fetch_data(url):
    with request.urlopen(url) as f:
        if f.status != 200:
            return False
        json_str = f.read()
        return json.loads(json_str)



# 测试

URL = 'https://yesno.wtf/api'
data = fetch_data(URL)
print(data)
assert data['answer'] == 'no'
print('ok')