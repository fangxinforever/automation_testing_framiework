#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fib(max):
    n, a, b = 0, 0, 1
    print("starting")
    while n < max:
        res = yield b
        a, b = b, a + b
        n = n + 1
        # print("res: ", res)
    return 'done'


if __name__ == '__main__':
    g = fib(6)
    print(next(g))
    # print(g.send(999))
    print(next(g))
