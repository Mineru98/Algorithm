# -*- coding:utf-8 -*-
import sys
from math import factorial

input = sys.stdin.readline


def bino_coef_factorial(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)


N, K = map(int, input().split())
print(bino_coef_factorial(N, K))
