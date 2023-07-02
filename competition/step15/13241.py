# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline
arr = list(map(int, input().split()))
A, B = arr
SMALLER, BIGGER = min(arr), max(arr)
MAX = A * B
if MAX == A or MAX == B:
    print(BIGGER)
else:
    A_arr = set(range(BIGGER, MAX + 1, BIGGER))
    B_arr = set(range(SMALLER, MAX + 1, SMALLER))
    print(min(A_arr & B_arr))
