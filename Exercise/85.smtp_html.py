#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

from_addr = 'bnyt_jane@163.com' #input('From...')
password  = '163jane163' #input('Password...')
to_addr = 'skylar.zhes@qq.com' #input('To:')
smtp_server = 'smtp.163.com' #input('SMTP server...')

msg = MIMEMultipart()

msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

with open(r'F:\projects\learn-python\Tutorial\static\image\tree.png','rb') as f:
    mime = MIMEBase('image','png',filename='tree.png')
    mime.add_header('Content-Disposition','attachment',filename='tree.png')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id','0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)
    msg.attach(MIMEText('<html><body><h1>Hello</h1><p>send by <a href="https://www.python.org">python</a></p><p><img src="cid:0"></p></body></html>', 'html', 'utf-8'))

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()