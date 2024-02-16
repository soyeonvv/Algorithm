from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt, value = 0, 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    graph[x][y] = 0
    queue.append((x, y))
    v = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
                    v += 1

    return v

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt += 1
            value = max(value, bfs(i, j))

print(cnt)
print(value)