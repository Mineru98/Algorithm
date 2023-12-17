# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline

a, b, k = list(map(int, input().split()))


import string


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


for n in range(a, b + 1):
    tmp = string.digits + string.ascii_lowercase
    print(convert(str(n), 2))

# arr = []
# count = 0
# for n in range(a, b + 1):
#     if n % k == 0:
#         tmp = []
#         for sn in str(n):
#             tmp.append(sn)
#         tmp.reverse()
#         tmp = "".join(tmp)
#         if tmp == str(n):
#             count += 1
# print(count)
