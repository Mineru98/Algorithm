# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
hear_set = set()
watch_set = set()
for _ in range(N):
    hear_set.add(input()[:-1])

for _ in range(M):
    watch_set.add(input()[:-1])

hear_and_watch_set = list(watch_set & hear_set)

print(len(hear_and_watch_set))
hear_and_watch_set = sorted(hear_and_watch_set)
for people in hear_and_watch_set:
    print(people)
