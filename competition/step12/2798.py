# -*- coding:utf-8 -*-
from itertools import combinations
N, M = list(map(int, input().split()))
num_str = list(map(int, input().split()[:N]))
num_str = list(combinations(num_str, 3))
total_str = list(map(sum, num_str))
total_str = list(filter(lambda x: x <= M, total_str))
total_str = sorted(total_str, reverse=True)
print(total_str[0])