# -*- coding:utf-8 -*-
import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    order_id, text = sys.stdin.readline().split()
    order_id = int(order_id)
    arr.append((order_id, text))
arr.sort(key=lambda x: (x[0], x[1] * -1))
for x, y in arr:
    print(x, y)
