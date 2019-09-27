#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

__author__ = 'guotengfei'
__time__ = 2019 / 9 / 27

"""
Module comment
"""

LOGGER = logging.getLogger(__name__)


def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    print(factorial(900))
