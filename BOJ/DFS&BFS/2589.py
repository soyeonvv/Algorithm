from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    visited = [[-1] * m for _ in range(n)]
    queue.append((x, y))
    visited[x][y] = 0

    time = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 'L' and visited[nx][ny] == -1:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    time = max(time, visited[nx][ny])

    return time

answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            answer = max(answer, bfs(i, j))

print(answer)