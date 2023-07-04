# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline


memo = []
check = [0] * (1000000 + 1)
check[0] = 1
check[1] = 1

for i in range(2, len(check)):
    if check[i] == 0:
        memo.append(i)
        for j in range(2 * i, len(check), i):
            check[j] = 1

T = int(input())
arr = []
for _ in range(T):
    count = 0
    n = int(input())
    for i in memo:
        if i >= n:
            break
        if not check[n - i] and i <= n - i:
            count += 1
    arr.append(count)

for num in arr:
    print(num)
