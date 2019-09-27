#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import random
import timeit

__author__ = 'guotengfei'
__time__ = 2019 / 9 / 27

"""

平均  O(n^2)

"""

LOGGER = logging.getLogger(__name__)


def select_sort(arr):
    sort_arr = []

    while len(arr) > 0:
        max = 0
        index = 0
        for i, value in enumerate(arr):
            if value > max:
                max = value
                index = i
        del arr[index]
        sort_arr.append(max)
    return sort_arr


if __name__ == '__main__':
    arr = random.sample(range(1000), 1000)
    print(arr)
    sort_arr = select_sort(arr)
    print(timeit.timeit(lambda: select_sort(arr), number=1))
    print(sort_arr)
