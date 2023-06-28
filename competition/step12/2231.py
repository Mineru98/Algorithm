# -*- coding:utf-8 -*-
N = int(input())
for i in range(1, N + 1): 
    num = sum((map(int, str(i))))
    print(num)
    num_sum = i + num
    if num_sum == N:
        print(i)
        break
    if i == N:
        print(0)