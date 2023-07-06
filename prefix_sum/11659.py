# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline


N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = {0: 0}
for i in range(N):
    sum_arr[i + 1] = sum_arr[i] + arr[i]
for _ in range(M):
    num_1, num_2 = map(int, input().split())
    if 1 <= num_1 <= num_2 <= N:
        print(sum_arr[num_2] - sum_arr[num_1 - 1])