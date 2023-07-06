# -*- coding:utf-8 -*-
import sys

input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
def bfs(y, x):
    rs = 1
    q = [(y, x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if graph_map[ny][nx] == 1 and visit_map[ny][nx] == False:
                    rs += 1
                    visit_map[ny][nx] = True
                    q.append((ny, nx))
    return rs

n, m = map(int, input().split())
graph_map = []
visit_map = [[False] * m for _ in range(n)] 

for _ in range(n):
    graph_map_item = list(map(int, input().split()))
    graph_map.append(graph_map_item)

cnt = 0
max_num = 0
for i in range(n):
    for j in range(m):
        if graph_map[i][j] == 1 and visit_map[i][j] == False:
            visit_map[i][j] = True
            cnt += 1
            max_num = max(max_num, bfs(i, j))
print(cnt)
print(max_num)