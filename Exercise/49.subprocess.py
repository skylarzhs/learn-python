#! /usr/bin/env python3
# -*- coding : utf-8 -*-

import subprocess

print('$ nslookup www.python.org')

r = subprocess.call(['nslookup','www.python.org'])

print('Exit code:',r)

# $ nslookup www.python.org
# 服务器:  UnKnown
# Address:  192.168.1.1

# 非权威应答:
# 名称:    dualstack.python.map.fastly.net
# Addresses:  2a04:4e42:36::223
#           151.101.108.223
# Aliases:  www.python.org

# Exit code: 0

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)