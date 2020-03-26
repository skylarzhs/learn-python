#!/usr/bin/env python3
# -*- encoding : utf-8 -*-


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            while n > 0:
                a, b = b, a + b
                n = n - 1
            return a
        elif isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start == None:
                start = 0
            a, b = 1, 1
            L = []
            for i in range(stop):
                if start >= i:
                    L.append(a)
                a, b = b, a + b
        return L


# for i in Fib():
#     print(i)

print(Fib()[0])
print(Fib()[1])
print(Fib()[2])
print(Fib()[3])
print(Fib()[4])
print(Fib()[5])
print(Fib()[6])
