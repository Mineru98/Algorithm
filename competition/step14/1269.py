# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline
_, __ = map(int, input().split())
A, B = set(map(int, input().split())), set(map(int, input().split()))
result = []
result.extend(A - B)
result.extend(B - A)
print(len(result))
