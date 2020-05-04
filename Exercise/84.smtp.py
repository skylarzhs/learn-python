#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

from_addr = input('From...')
password  = input('Password...')
to_addr = input('To:')
smtp_server = input('SMTP server...')

msg = MIMEText('您有新的订单通知，请登录平台查看！', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()


server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

# send: 'ehlo [192.168.56.1]\r\n'
# reply: b'250-mail\r\n'
# reply: b'250-PIPELINING\r\n'
# reply: b'250-AUTH LOGIN PLAIN \r\n'
# reply: b'250-AUTH=LOGIN PLAIN\r\n'
# reply: b'250-coremail 1Uxr2xKj7kG0xkI17xGrU7I0s8FY2U3Uj8Cz28x1UUUUU7Ic2I0Y2UrZC1H8UCa0xDrUUUUj\r\n'
# reply: b'250-STARTTLS\r\n'
# reply: b'250 8BITMIME\r\n'
# reply: retcode (250); Msg: b'mail\nPIPELINING\nAUTH LOGIN PLAIN\nAUTH=LOGIN PLAIN\ncoremail 1Uxr2xKj7kG0xkI17xGrU7I0s8FY2U3Uj8Cz28x1UUUUU7Ic2I0Y2UrZC1H8UCa0xDrUUUUj\nSTARTTLS\n8BITMIME'
# send: 'AUTH PLAIN AGJueXRfamFuZUAxNjMuY29tADE2M2phbmUxNjM=\r\n'
# reply: b'235 Authentication successful\r\n'
# reply: retcode (235); Msg: b'Authentication successful'
# send: 'mail FROM:<example@163.com>\r\n'
# reply: b'250 Mail OK\r\n'
# reply: retcode (250); Msg: b'Mail OK'
# send: 'rcpt TO:<example@qq.com>\r\n'
# reply: b'250 Mail OK\r\n'
# reply: retcode (250); Msg: b'Mail OK'
# send: 'data\r\n'
# reply: b'354 End data with <CR><LF>.<CR><LF>\r\n'
# reply: retcode (354); Msg: b'End data with <CR><LF>.<CR><LF>'
# data: (354, b'End data with <CR><LF>.<CR><LF>')
# send: b'Content-Type: text/plain; charset="utf-8"\r\nMIME-Version: 1.0\r\nContent-Transfer-Encoding: base64\r\nFrom: =?utf-8?b?UHl0aG9u54ix5aW96ICF?= <example@163.com>\r\nTo: =?utf-8?b?566h55CG5ZGY?= <example@qq.com>\r\nSubject: =?utf-8?b?5p2l6IeqU01UUOeahOmXruWAmeKApuKApg==?=\r\n\r\n5oKo5pyJ5paw55qE6K6i5Y2V6YCa55+l77yM6K+355m75b2V5bmz5Y+w5p+l55yL77yB\r\n.\r\n'
# reply: b'250 Mail OK queued as smtp5,HdxpCgCnm++Lt69e8otkAw--.262S2 1588574103\r\n'reply: retcode (250); Msg: b'Mail OK queued as smtp5,HdxpCgCnm++Lt69e8otkAw--.262S2 1588574103'
# data: (250, b'Mail OK queued as smtp5,HdxpCgCnm++Lt69e8otkAw--.262S2 1588574103')
# send: 'quit\r\n'
# reply: b'221 Bye\r\n'
# reply: retcode (221); Msg: b'Bye'
