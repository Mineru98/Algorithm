# -*- coding:utf-8 -*-
# 푸는 중(이분 탐색으로 시도중)
import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))
woods = list(map(int, input().split()))
max_h, min_h = max(woods), min(woods)
control_h = max_h - int(abs(max_h - M) / 2)
count = 0
while True:
    print("control_h", control_h)
    calc = sum(list(filter(lambda x: x >= 0, map(lambda x: x - control_h, woods))))
    if calc == M:
        print("control_h:", control_h)
        break
    elif calc > M:
        print("1. sum:", calc)
        control_h += int((max_h - control_h) / 2)
        print("2:", control_h)
    else:
        print("3. sum:", calc)
        control_h -= int((control_h - N) / 2)
        print("4:", control_h)
    count += 1
    if count > 10:
        break
