# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline

N = int(input())
step = int(input())

arr = []
for _ in range(N - 1):
    num = int(input())
    arr.append(num)
count = 0
for i in range(1, len(arr)):
    A, B = arr[i - 1], arr[i]
    if (B - A) // 2 > 1:
        count += (B - A) // 2 - 1
print(count)