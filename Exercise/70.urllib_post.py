#!/usr/bin/env python3
# -*- coding : utf-8 -*-

from urllib import request,parse

print('Login into boss')

mobile = input('Mobile...')
verify = input('Verify...')

login_data = parse.urlencode([
    ('mobile',mobile),
    ('verify',verify),
    ('type','verify'),
    ('role','member'),
    ('ref','Skylar'),
])

req = request.Request('https://dmpweb.drbroker.net/api/user/login')
req.add_header('Referer','https://dmpweb.drbroker.net/member/login')

with request.urlopen(req,data=login_data.encode('utf-8')) as f:
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s' % (k,v))
    print('Data',f.read().decode('utf-8'))

# Login into boss
# Mobile...13245485672
# Verify...111111
# Status: 200 OK
# Date:Fri, 24 Apr 2020 12:53:12 GMT
# Server:Apache/2.4.39 (Unix) OpenSSL/1.0.2r PHP/7.1.29 mod_perl/2.0.8-dev Perl/v5.16.3
# X-Powered-By:PHP/7.1.29
# Cache-Control:no-cache, private
# Set-Cookie:bnyt_session=EYjrQc23Clt9TDpZER3sZ5o9vrhroKLpTIwkQnx4; expires=Fri, 24-Apr-2020 14:53:13 GMT; Max-Age=7200; path=/; httponly
# Content-Length:124
# Connection:close
# Content-Type:application/json
# Data {"code":200,"message":"\u4fe1\u606f\u5904\u7406\u6210\u529f","data":{"id":"9553","mid":"9553","expertId":0,"role":"member"}}