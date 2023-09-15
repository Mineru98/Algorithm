# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline

result = []

n = -1
while n != 0:
    n = int(input())
    names = {}
    names_arr = []
    for _ in range(n):
        name = input().strip()
        names[name] = 2
        names_arr.append(name)
    for _ in range(2 * n - 1):
        idx, s = list(input().split())
        idx = int(idx)
        names[names_arr[idx - 1]] -= 1
    for name in names.keys():
        if names[name] != 0:
            result.append(name)
            break

for i, name in enumerate(result):
    print(i + 1, name)
