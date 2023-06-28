# -*- coding:utf-8 -*-
import string
N, B = map(int, input().split())
s = ''
arr = "0123456789"+string.ascii_uppercase

while N:
    s += str(arr[N%B])
    N //= B

print(s[::-1])