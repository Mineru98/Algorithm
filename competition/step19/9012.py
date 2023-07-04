# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    last_idx = 0
    pattern = input()[:-1]
    if pattern.startswith(")") or len(pattern) % 2 == 1:
        print("NO")
    else:
        check_sum = False
        for w in pattern:
            if w == "(":
                last_idx += 1
            else:
                last_idx -= 1
            if last_idx == -1:
                print("NO")
                check_sum = True
                break
        if last_idx == 0:
            print("YES")
        elif check_sum:
            continue
        else:
            print("NO")
