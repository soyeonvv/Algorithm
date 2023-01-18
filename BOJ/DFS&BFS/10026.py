# BFS
from collections import deque

def bfs(x, y):
    queue.append((x, y))
    visited[x][y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        qx, qy = queue.popleft()
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[qx][qy] == graph[nx][ny] and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

n = int(input())
graph = [list(input()) for _ in range(n)]
queue = deque()

# 정상인
visited = [[0] * n for _ in range(n)]
cnt1 = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            cnt1 += 1
            bfs(i, j)

# 적록색약
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

visited = [[0] * n for _ in range(n)]
cnt2 = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            cnt2 += 1
            bfs(i, j)

print(cnt1, cnt2)

'''
# DFS
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[x][y] == graph[nx][ny] and visited[nx][ny] == 0:
                dfs(nx, ny)


n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
# 정상인
cnt1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            cnt1 += 1
            dfs(i, j)
# 적록색약
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'
cnt2 = 0
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            cnt2 += 1
            dfs(i, j)

print(cnt1, cnt2)
'''