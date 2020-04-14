#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import re

def is_valid_email(email):
    re_email = re.compile(r'^[\w\.\_]{3,}@\w{3,}(\.\w{3,})*$')
    ret = re_email.match(email)
    if ret is None:
        return False
    return True

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')