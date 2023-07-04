# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline

N = int(input())
input()
enter = dict()
enter_set = set()
for _ in range(N - 1):
    word = input()[:-1]
    if word != "ENTER":
        if word in enter.keys():
            if word not in enter_set:
                enter[word] += 1
        else:
            enter[word] = 1
        enter_set.add(word)
    else:
        enter_set.clear()

print(sum(enter.values()))
