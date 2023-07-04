# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline

_ = int(input())
num_arr = list(map(int, input().split()))
min_num, max_num = min(num_arr), max(num_arr)
print(min_num * max_num)
