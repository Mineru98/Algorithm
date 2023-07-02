# -*- coding:utf-8 -*-
N, k = list(map(int, input().split()))
score_list = list(map(int, input().split()))
score_list = score_list[:N]
score_list.sort(reverse=True)
print(score_list[k - 1])
