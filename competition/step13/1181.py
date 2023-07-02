# -*- coding:utf-8 -*-
import sys

arr = set()
N = int(sys.stdin.readline())
for _ in range(N):
    word = sys.stdin.readline()
    arr.add(word[:-1])
arr = list(arr)
arr.sort(key=lambda x: (len(x), x))
for word in arr:
    print(word)
