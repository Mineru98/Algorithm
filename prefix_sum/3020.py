# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline


N, H = map(int, input().split())
down = [0] * (H + 1)
up = [0] * (H + 1)

if 2 <= N <= 200000 and 2 <= H <= 500000:
    for i in range(N):
        height = int(input())
        if (i % 2 == 0):
            down[height] += 1
        else:
            up[height] += 1
for i in range(H - 1, 0, -1):
    down[i] += down[i+1]
    up[i] += up[i+1]
print(down, up)

min_count = N
same_height = 0

for i in range(1, H + 1):
    if (min_count > down[i] + up[H - i + 1]):
        min_count = down[i] + up[H - i + 1]
        same_height = 1
    elif (min_count == down[i] + up[H - i + 1]):
        same_height += 1

print(min_count, same_height)