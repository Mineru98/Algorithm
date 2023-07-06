# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort(reverse=True)
count = 0

for item in arr:
    count += K // item
    K = K % item
print(count)