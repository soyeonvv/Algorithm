# DFS
import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, h):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[x][y] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] > h and visited[nx][ny] == 0:
                dfs(nx, ny, h)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

result = 0

for h in range(max(map(max, graph)) + 1):
    cnt = 0
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and visited[i][j] == 0:
                cnt += 1
                dfs(i, j, h)

    result = max(result, cnt)

print(result)

'''
# BFS
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, h):
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        qx, qy = queue.popleft()
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > h and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

result = 0

for h in range(max(map(max, graph)) + 1):
    cnt = 0
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and visited[i][j] == 0:
                cnt += 1
                bfs(i, j, h)

    result = max(result, cnt)

print(result)
'''