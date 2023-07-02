# -*- coding:utf-8 -*-
import sys

N = int(sys.stdin.readline())
arr_1 = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
arr_2 = list(map(int, sys.stdin.readline().split()))

result = {}
for i in range(len(arr_1)):
    result[arr_1[i]] = 0

for j in range(M):
    if arr_2[j] not in result:
        print(0, end=" ")
    else:
        print(1, end=" ")
