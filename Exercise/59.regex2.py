#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import re


def name_of_email(email):
    regex_name = re.compile(
        r'^(\<([A-Z][a-z]{2,}\s[A-Z][a-z]{2,})\>\s)?(\w{3,})@\w{3,}(\.\w{3,})*$')
    ret = regex_name.match(email)
    if ret is None:
        return False
    if ret.group(2) is not None and ret.group(2) != '':
        return ret.group(2)
    elif ret.group(3) is not None and ret.group(3) != '':
        return ret.group(3)
    else:
        return False


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
