# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline

K = int(input())

arr = []
for _ in range(K):
    num = int(input())
    if num == 0:
        if len(arr) > 0:
            arr.pop(len(arr) - 1)
    else:
        arr.append(num)
print(sum(arr))
