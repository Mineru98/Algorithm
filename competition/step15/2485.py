# -*- coding:utf-8 -*-
import sys
from math import gcd

input = sys.stdin.readline

N = int(input())
first = int(input())

arr = []
for i in range(N - 1):
    num = int(input())
    arr.append(num - first)
    first = num

g = arr[0]
for j in range(1, len(arr)):
    g = gcd(g, arr[j])

result = 0
for each in arr:
    result += each // g - 1
print(result)
