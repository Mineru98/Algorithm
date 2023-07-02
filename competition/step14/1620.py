# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline
N, M = list(map(int, input().split()))
pocket_manster_str = {}
pocket_manster_int = {}

for idx in range(N):
    pocket_manster = input()[:-1]
    pocket_manster_str[pocket_manster] = idx + 1
    pocket_manster_int[idx + 1] = pocket_manster
result = []
for _ in range(M):
    val = input()[:-1]
    try:
        idx = int(val)
        result.append(pocket_manster_int[idx])
    except:
        result.append(pocket_manster_str[val])

for item in result:
    print(item)
