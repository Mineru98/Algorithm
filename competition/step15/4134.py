# -*- coding:utf-8 -*-
import sys
import math

input = sys.stdin.readline


def check(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


case_num = int(input())
arr = []
for _ in range(case_num):
    n = int(input())
    arr.append(n)

for n in arr:
    while True:
        if check(n):
            print(n)
            break
        else:
            n += 1
