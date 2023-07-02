# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline
cnt = int(input())

result = []
for _ in range(cnt):
    arr = list(map(int, input().split()))
    A, B = arr
    SMALLER, BIGGER = min(arr), max(arr)
    MAX = A * B
    if MAX == A or MAX == B:
        result.append(BIGGER)
    else:
        A_arr = set(range(BIGGER, MAX + 1, BIGGER))
        B_arr = set(range(SMALLER, MAX + 1, SMALLER))
        result.append(min(A_arr & B_arr))
for item in result:
    print(item)
