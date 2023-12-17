# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline

count = int(input())

members = {}
for _ in range(count):
    name = input().strip()
    part = input().strip()
    members[name] = {"part": part, "vote_count": 0}

count = int(input())
for _ in range(count):
    name = input().strip()
    try:
        members[name]["vote_count"] += 1
    except:
        pass

max_vote_count = max(list(map(lambda x: x[1]["vote_count"], members.items())))
arr = list(filter(lambda x: x[1]["vote_count"] == max_vote_count, members.items()))
if len(arr) == 1:
    print(arr[0][1]["part"], end="")
elif len(arr) > 1:
    print("tie", end="")
else:
    print("", end="")
