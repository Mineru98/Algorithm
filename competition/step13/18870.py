# -*- coding:utf-8 -*-
import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
arr = arr[:N]
arr_set = set(arr)
arr_order = sorted(list(arr_set))
arr_set = None
arr_dict = {}
for i, k in enumerate(arr_order):
    arr_dict[k] = i
arr = [str(arr_dict[i]) for i in arr]
print(" ".join(arr))
