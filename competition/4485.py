# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline

while True:
    N = int(input())
    if N == 0:
        break
    else:
        arr = []
        for _ in range(N):
            arr.append(list(map(int, input().split())))
