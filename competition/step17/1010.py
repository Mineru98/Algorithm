# -*- coding:utf-8 -*-
import sys
from math import factorial

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    bridge = factorial(M) // (factorial(N) * factorial(M - N))
    print(bridge)
