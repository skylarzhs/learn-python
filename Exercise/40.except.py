from functools import reduce

def str2num(s):
    # return int(s)
    try:
        i = int(s)
    except ValueError:
        i = float(s)
    else:
        return i
    finally:
        pass

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()