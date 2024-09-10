from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

cheese = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cheese += 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and graph[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                elif graph[nx][ny] == 1:
                    visited[nx][ny] += 1

def melt():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                graph[i][j] = 0
                cnt += 1
    return cnt

time = 0
while True:
    visited = [[0] * m for _ in range(n)]
    bfs(0, 0)
    time += 1

    cheese -= melt()
    if cheese == 0:
        break

print(time)