# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline

# N은 재고, M은 구매자 수
N, M = list(map(int, input().split()))

# 구매자들의 원하는 가격
want_price = []
for _ in range(M):
    val = int(input())
    want_price.append([val, None])

want_price.sort(key=lambda x: x[0] * -1)
for i, item in enumerate(want_price):
    price, pred_max_amount = item
    peoples = list(filter(lambda x: x[0] >= price, want_price))
    want_price[i][1] = price * min([len(peoples), N])
want_price.sort(key=lambda x: x[1] * -1)
print(want_price[0][0], want_price[0][1])
