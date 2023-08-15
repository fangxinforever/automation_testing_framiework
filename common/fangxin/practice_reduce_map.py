#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def fn(x, y):
    return x * 10 + y


def char2num(s):
    return DIGITS[s]


if __name__ == '__main__':
    print(reduce(fn, list(map(char2num, '13579'))))
    print(type(reduce(fn, list(map(char2num, '13579')))))

