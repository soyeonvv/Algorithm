from collections import deque

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(value, queue, visited):
    while queue:
        x, y, time = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] != '#' and graph[nx][ny] != '*':
                    if visited[nx][ny] > time + 1:
                        queue.append((nx, ny, time + 1))
                        visited[nx][ny] = time + 1
            elif value:
                print(time + 1)
                return
    if value:
        print('IMPOSSIBLE')

for _ in range(t):
    w, h = map(int, input().split())
    graph = [list(input()) for _ in range(h)]
    visited = [[int(1e9)] * w for _ in range(h)]
    sangeun, fire = deque(), deque()
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '@':
                sangeun.append((i, j, 0))
            elif graph[i][j] == '*':
                fire.append((i, j, 0))
                visited[i][j] = 0

    # 불 먼저 이동
    bfs(0, fire, visited)
    # 상근이 이동
    bfs(1, sangeun, visited)