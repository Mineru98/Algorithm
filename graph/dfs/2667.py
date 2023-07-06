# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
def dfs(y, x):
    global each
    each += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < n and 0 <= nx < n:
            if graph_map[ny][nx] == 1 and visit_map[ny][nx] == False:
                visit_map[ny][nx] = True
                dfs(ny, nx)

n = int(input())
graph_map = [list(map(int, input().strip())) for _ in range(n)]
visit_map = [[False] * n for _ in range(n)] 
result = []
each = 0

for i in range(n):
    for j in range(n):
        if graph_map[i][j] == 1 and visit_map[i][j] == False:
            visit_map[i][j] = True
            each = 0
            dfs(i, j)
            result.append(each)
result.sort()
print(len(result))
for item in result:
    print(item)