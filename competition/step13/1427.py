# -*- coding:utf-8 -*-
import sys

N = sys.stdin.readline()
arr = []
for n in N[:-1]:
    arr.append(int(n))
arr.sort(reverse=True)
arr = "".join(map(str, arr))
print(arr)
