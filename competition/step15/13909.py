# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline

N = int(input())

arr = [0] * N
for i in range(1, len(arr) + 1):
    for j in range(i, len(arr) + 1, i):
        if j % i == 0:
            if arr[j - 1] == 0:
                arr[j - 1] = 1
            else:
                arr[j - 1] = 0
print(sum(arr))

print(int(int(input()) ** 0.5))
