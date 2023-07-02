# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
s = set([input() for _ in range(N)])
count = 0
for _ in range(M):
    t = input()
    if t in s:
        count += 1
print(count)
