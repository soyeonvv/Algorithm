from collections import deque

n, m, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    time = []
    queue = deque()
    visited = [[-1] * m for _ in range(n)]
    queue.append((0, 0))
    visited[0][0] = 0

    while queue:
        x, y = queue.popleft()
        if visited[x][y] > t:
            continue
        if (x, y) == (n - 1, m - 1):
            time.append(visited[x][y])
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    if graph[nx][ny] == 2 and visited[nx][ny] + (n - 1 - nx) + (m - 1 - ny) <= t:
                        time.append(visited[nx][ny] + (n - 1 - nx) + (m - 1 - ny))
                        continue
                    queue.append((nx, ny))

    if len(time) == 0:
        print("Fail")
    else:
        print(min(time))

bfs()