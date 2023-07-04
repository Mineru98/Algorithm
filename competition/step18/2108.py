# -*- coding:utf-8 -*-
import sys
import statistics as st

input = sys.stdin.readline


def mode(arr: list):
    counter = {}
    for item in arr:
        if item not in counter.keys():
            counter[item] = 1
        else:
            counter[item] += 1
    max_num = max(counter.values())
    max_dic = []
    for i in counter:
        if max_num == counter[i]:
            max_dic.append(i)
    if len(max_dic) > 1:
        return max_dic[1]
    else:
        return max_dic[0]


N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))


arr.sort()

print(round(st.mean(arr)))
print(st.median(arr))
print(mode(arr))
print(max(arr) - min(arr))
