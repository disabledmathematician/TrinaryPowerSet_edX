# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 00:36:44 2023

@author: Charles_Truscott
"""

def return_trinary(n, nl):
    s = ''
    for x in range(nl, -1, -1):
        if n // (2 * (3 ** x)) == 1:
            s += '2'
            n -= 2 * (3 ** x)
        elif n // (3 ** x) == 1:
            s += '1'
            n -= 3 ** x
        else:
            s += '0'
            n -= 0
    print(s)
    return s

def powerset_two_sorts():
    L = ["apples", "pears", "peaches", "bananas"]
    first = []
    second = []
    for x in range(3 ** (len(L)), -1, -1):
        s = return_trinary(x, len(L) - 1)
        temp_first =[]
        temp_second =[]
        for y in range(len(s) - 1, -1, -1):
            if s[y] == '2':
                temp_second.append(L[y])
            elif s[y] == '1':
                temp_first.append(L[y])
        second.append(temp_second)
        first.append(temp_first)
    print("First: {} Second: {}".format(first, second))

if __name__ == "__main__": powerset_two_sorts()