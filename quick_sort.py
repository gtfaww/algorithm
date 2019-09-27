#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import timeit

__author__ = 'guotengfei'
__time__ = 2019 / 9 / 27

"""
平均： O(n log n)
最差  O(n^2)
"""


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = random.choice(arr)
    min = [m for m in arr if m <= pivot]
    max = [m for m in arr if m > pivot]
    return quick_sort(min) + quick_sort(max)


if __name__ == '__main__':
    arr = random.sample(range(1000), 1000)
    pivot = random.choice(arr)
    print(arr)
    print(quick_sort(arr))
    print(timeit.timeit(lambda: quick_sort(arr), number=1))
