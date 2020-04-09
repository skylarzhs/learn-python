# -*- coding : utf-8 -*-

# 练习
# 利用os模块编写一个能实现dir -l输出的程序。

# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
# drwxrwxr-x 3 bnyttools bnyttools    4096 Jun 29  2019 api
# drwxrwxr-x 2 bnyttools bnyttools    4096 Apr  9 02:00 backups
# -rw-rw-r-- 1 bnyttools bnyttools    5617 Jun 11  2019 bnyt_165server.ovpn

# import os
# import time

# for f in os.listdir('.'):
#     fileinfo = os.stat(f)
#     mtime = time.strftime('%b %d %H:%I', time.localtime(fileinfo.st_mtime))
#     if os.path.isdir(f):
#         ft = 'd'
#     else:
#         ft = '-'
#     print('%s mode=%s %s %d %s %s' % (ft, fileinfo.st_mode,
#                                       fileinfo.st_nlink, fileinfo.st_size, mtime, f))

# 执行情况：Linux下执行正常；Windows下文件数目显示不正确

import os

print(os.path.abspath('.'))

print(os.path.isdir('.\Exercise\__pycache__'))

def findfile(str, path='.'):
    for f in os.listdir(path):
        npath = os.path.join(path, f)
        print('npath = %s isdir ret = %s' % (npath,int(os.path.isdir(f))))
        if os.path.isdir(f):
            print('newpath = %s' % npath)
            findfile(str, npath)
        else:
            if npath.find(str) == -1:
                continue
            else:
                print('find one! path = %s' % npath)


# 遍历二级目录有问题

findfile('py')