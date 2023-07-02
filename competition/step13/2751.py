# -*- coding:utf-8 -*-
import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    num = int(sys.stdin.readline())
    arr.append(num)
arr.sort()

for i in arr:
    print(i)
