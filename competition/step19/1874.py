# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline

n = int(input())

stack = []
answer = []
check_sum = False
cur = 1
for i in range(n):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        answer.append("+")
        cur += 1

    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        check_sum = True
        break

if not check_sum:
    for i in answer:
        print(i)
