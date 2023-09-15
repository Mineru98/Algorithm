# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline

p_count = -1
while p_count != 0:
    p_count = int(input())
    eval_arr = {}
    p_arr = []
    for i in range(p_count):
        lit = list(input().split())
        eval_arr[lit[0]] = {"eval": lit[1:p_count], "order": []}
        p_arr.append(lit[0])
    print(eval_arr)
    idx = 0
    for name in eval_arr.keys():
        for i, eval_item in enumerate(eval_arr[name]):
            p_count % i
        idx += 1
