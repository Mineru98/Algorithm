# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline

N = int(input())

idx = -1
arr = []
for _ in range(N):
    line = input().split()
    if len(line) == 2:
        action, num = line
        num = int(num)
    else:
        action = line[0]
    if action == "push":
        arr.append(num)
    elif action == "top":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[len(arr) - 1])
    elif action == "size":
        print(len(arr))
    elif action == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif action == "pop":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
