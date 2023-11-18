from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def melting():
    melt = [[0] * m for _ in range(n)]
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if graph[i][j] != 0:
                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    if graph[nx][ny] == 0:
                        melt[i][j] += 1
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if melt[i][j] != 0:
                graph[i][j] -= melt[i][j]
                if graph[i][j] < 0:
                    graph[i][j] = 0

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and graph[nx][ny] != 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1

def counting():
    c = 0
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if graph[i][j] != 0 and visited[i][j] == 0:
                bfs(i, j)
                c += 1
    return c

time = 0
while True:
    time += 1

    # 빙산 녹음
    melting()

    # 빙산 덩어리 개수 계산
    visited = [[0] * m for _ in range(n)]
    cnt = counting()

    if cnt == 0:
        time = 0
        break
    if cnt >= 2:
        break

print(time)