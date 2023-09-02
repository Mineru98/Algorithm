# -*- coding:utf-8 -*-
import sys
from itertools import groupby

input = sys.stdin.readline

T = int(input())
count = 0
for _ in range(T):
    n, m, c = list(map(int, input().split()))
    data_type = list(range(1, m + 1))
    data_cost = list(map(int, input().split()))
    cost_arr = list(map(int, input().split()))
    grouped = groupby(cost_arr)

# 12 3 12
# 2 2 4
# 1 1 1 1 1 2 2 2 3 2 1 2

# 1: 5 * 2 > c
# 2: 3 * 2 > c
# 3: 1 * 4 > c
# 2: 1 * 2 > c
# 1: 1 * 2 > c
# 2: 1 * 2 > c
