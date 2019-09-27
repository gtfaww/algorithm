#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools
import timeit

__author__ = 'guotengfei'
__time__ = 2019 / 9 / 27

"""
Module comment
"""


@functools.lru_cache()
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fib_loop(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def fib_gen(n):
    a, b = 0, 1
    while n > 0:
        yield a
        n -= 1
        a, b = b, a + b


if __name__ == '__main__':
    print(fibonacci(10))
    print(fib_loop(10))
    print(timeit.timeit(lambda: fibonacci(40), number=1))
    print(timeit.timeit(lambda: fib_loop(40), number=1))
    for i in fib_gen(11):
        print(i)
