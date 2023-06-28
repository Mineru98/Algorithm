# -*- coding:utf-8 -*-
import string
N, B = input().split()
N = ''.join(reversed(N))
B = int(B)

str_number = "0123456789"+string.ascii_uppercase
result = 0

for x in range(len(N) -1, -1, -1):
    total_sum = str_number.index(N[x]) * (B**x)
    result += total_sum

print(result)