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


all_list = list(range(2, 123456 * 2))
memo = []

for i in all_list:
    if check(i):
        memo.append(i)

n = int(input())

while True:
    count = 0
    if n == 0:
        break
    for i in memo:
        if n < i <= 2 * n:
            count += 1
    print(count)
    n = int(input())
