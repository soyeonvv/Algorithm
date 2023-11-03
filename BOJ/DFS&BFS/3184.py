from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    o, v = 0, 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] != '#' and visited[nx][ny] != 1:
                    if graph[nx][ny] == 'o':
                        o += 1
                    elif graph[nx][ny] == 'v':
                        v += 1
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

    global r_sheep, r_wolf
    if o > v:
        r_wolf += v
    else:
        r_sheep += o

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]

visited = [[0] * c for _ in range(r)]

sheep, wolf, r_sheep, r_wolf = 0, 0, 0, 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'o':
            sheep += 1
        if graph[i][j] == 'v':
            wolf += 1
            if visited[i][j] == 0:
                bfs(i, j)

print(sheep - r_sheep, wolf - r_wolf)