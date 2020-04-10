#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import os

print('Process (%s) starting...' % os.getpid())

pid = os.fork()
print('pid = %s' % pid)
if pid == 0:
	print('I am child process (%s),and my parent is (%s)' % (os.getpid(),os.getppid()))
else:
	print('I(%s) just created a child process (%s)' % (os.getpid(),pid))

#Process (3800) starting...
#pid = 3801
#I(3800) just created a child process (3801)
#pid = 0
#I am child process (3801),and my parent is (3800)

