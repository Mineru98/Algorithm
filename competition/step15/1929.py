# -*- coding:utf-8 -*-
import sys
import math

input = sys.stdin.readline


def check(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


M, N = list(map(int, input().split()))

for i in range(M, N + 1):
    if check(i):
        print(i)
