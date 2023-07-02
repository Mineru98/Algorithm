# -*- coding:utf-8 -*-
arr = []
arr_sum = 0
for _ in range(5):
    num = int(input())
    arr.append(num)
arr.sort()
arr_avg = int(sum(arr) / len(arr))
print(arr_avg)
print(arr[2])
