# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline

N = int(input())
arr = {}
for _ in range(N):
    people, action = input().split()
    if action == "enter":
        arr[people] = None
    elif action == "leave":
        del arr[people]
for people in sorted(arr.keys(), reverse=True):
    print(people)
