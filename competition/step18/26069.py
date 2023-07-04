# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline

N = int(input())

competitions = {"ChongChong": 1}

for _ in range(N):
    A, B = input().split()
    if A not in competitions.keys():
        competitions[A] = 0
    if B not in competitions.keys():
        competitions[B] = 0
    if competitions[B]:
        competitions[A] = 1
    if competitions[A]:
        competitions[B] = 1

print(sum(competitions.values()))
