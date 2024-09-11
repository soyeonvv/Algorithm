from collections import deque

n, m, k = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))
    visited[x][y][z] = 1

    while queue:
        x, y, z = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][z]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1 and z < k and visited[nx][ny][z + 1] == 0:
                queue.append((nx, ny, z + 1))
                visited[nx][ny][z + 1] = visited[x][y][z] + 1
            elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                queue.append((nx, ny, z))
                visited[nx][ny][z] = visited[x][y][z] + 1

    return -1

print(bfs(0, 0, 0))