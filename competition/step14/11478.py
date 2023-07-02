# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline

word_list = [w for w in input()[:-1]]
result = []
for i in range(len(word_list), -1, -1):
    for j in range(i + 1):
        result.append("".join(word_list[j:i]))
result = set(filter(lambda x: len(x) > 0, result))
print(len(result))
