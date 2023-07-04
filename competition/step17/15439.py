# -*- coding:utf-8 -*-
import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

sets = list(permutations([i for i in range(N)], 2))
print(len(sets))
