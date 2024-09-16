from collections import deque

k = int(input())
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]
visited = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]

hx = [-2, -2, -1, -1, 1, 1, 2, 2]
hy = [-1, 1, -2, 2, -2, 2, -1, 1]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))
    visited[x][y][z] = 1

    while queue:
        x, y, z = queue.popleft()
        if x == h - 1 and y == w - 1:
            return visited[x][y][z] - 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny][z] == graph[nx][ny] == 0:
                queue.append((nx, ny, z))
                visited[nx][ny][z] = visited[x][y][z] + 1

        if z < k:
            for i in range(8):
                nx, ny = x + hx[i], y + hy[i]
                if 0 <= nx < h and 0 <= ny < w and visited[nx][ny][z + 1] == graph[nx][ny] == 0:
                    queue.append((nx, ny, z + 1))
                    visited[nx][ny][z + 1] = visited[x][y][z] + 1

    return -1

print(bfs(0, 0, 0))