# -*- coding:utf-8 -*-
import sys


def gcd(x, y):
    mod = x % y
    while mod > 0:
        x = y
        y = mod
        mod = x % y
    return y


input = sys.stdin.readline
A, B = list(map(int, input().split()))
C, D = list(map(int, input().split()))

N = gcd(A * D + C * B, B * D)
print((A * D + C * B) // N, B * D // N)
