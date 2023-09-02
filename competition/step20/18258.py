# -*- coding:utf-8 -*-
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

queue = deque([])
for _ in range(N):
    line = input().split()
    if len(line) == 2:
        action, num = line
        num = int(num)
    else:
        action = line[0]
    if action == "push":
        queue.append(num)
    elif action == "front":
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    elif action == "back":
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)
    elif action == "size":
        print(len(queue))
    elif action == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif action == "pop":
        if len(queue) > 0:
            print(queue.popleft())
        else:
            print(-1)
