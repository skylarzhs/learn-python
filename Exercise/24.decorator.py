# -*- coding : utf-8 -*-


# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s()' % func.__name__)
#         return func(*args, **kw)
#     return wrapper


# @log # now = log(now)
# def now():
#     print('2020-03-23')


# now()

# decorator中传入参数
# import functools

# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator


# @log('Execute')  # log('Execute')(now)
# def now():
#     print('2020-03-23')


# now()

# print(now.__name__) # wrapper

import time
# import functools


# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args, **kw):
#         print('%s executed in %s ms' % (fn.__name__, round(time.time()*1000)))
#         return fn(*args, **kw)
#     return wrapper

# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y

# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z

# f = fast(11, 22)
# s = slow(11, 22, 33)


# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')
# else:
#     print('测试成功！')

import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('%s executed in %s ms' %
              (func.__name__, time.time()))
        ret = func(*args, **kw)
        time.sleep(1)
        print('%s executed in %s ms' %
              (func.__name__, time.time()))

        return ret
    return wrapper


@log
def test():
    print('excuting...')


test()
