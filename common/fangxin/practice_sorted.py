#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return str.lower(t[0])


if __name__ == '__main__':
    list1 = [36, 5, -12, 9, -21]
    print(sorted(list1, key=abs))
    list2 = ['bob', 'about', 'Zoo', 'Credit']
    print(sorted(list2, key=str.lower))
    L2 = sorted(L, key=by_name)
    print(L2)

