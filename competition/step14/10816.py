# -*- coding:utf-8 -*-
import sys

_ = int(sys.stdin.readline())
N = list(map(int, sys.stdin.readline().split()))

_ = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))

result = {}
for n in N:
    if n in result:
        result[n] += 1
    else:
        result[n] = 1
print(" ".join(str(result[m]) if m in result else "0" for m in M))
