# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline

r, c = map(int, input().split())
arr = []
for _ in range(r):
    arr.append(list(input().strip()))

ans = 0
alphas = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x=0, y=0, count=1):
    global ans
    ans = max(ans, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not arr[nx][ny] in alphas:
            alphas.add(arr[nx][ny])
            dfs(nx, ny, count + 1)
            alphas.remove(arr[nx][ny])


alphas.add(arr[0][0])
dfs(0, 0)
print(ans)
