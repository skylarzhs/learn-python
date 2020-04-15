#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import base64


# def safe_base64_decode(s):
#     if isinstance(s, str):
#         new_str = s
#     elif isinstance(s, bytes):
#         new_str = s.decode('ascii')
#     else:
#         raise(ValueError)
#     slen = len(s)
#     L = [new_str]
#     less = 4 - slen % 4
#     if less < 4:
#         for i in range(less):
#             L.append('=')
#     new_str = str(L).encode('ascii')
#     return base64.b64decode(new_str)

# 评论区参考

def safe_base64_decode(s):
    while len(s) % 4 > 0:
        s = s + b'='
    return base64.b64decode(s)


# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
