# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = dict()
for _ in range(N):
    word = input()[:-1]
    if len(word) >= M:
        if word in arr.keys():
            arr[word] += 1
        else:
            arr[word] = 1
for word, count in sorted(arr.items(), key=lambda item: (-item[1], -len(item[0]), item[0])):
    print(word)
