from collections import deque

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]

water = [[-1] * c for _ in range(r)]
dist = [[-1] * c for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def water_bfs():
    queue = deque()

    for i in range(r):
        for j in range(c):
            if graph[i][j] == '*':
                queue.append((i, j))
                visited[i][j] = 1
                water[i][j] = 0
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c: continue
            if graph[nx][ny] != '.': continue
            if visited[nx][ny] == 1: continue
            queue.append((nx, ny))
            visited[nx][ny] = 1
            water[nx][ny] = water[x][y] + 1

def bfs():
    queue = deque()

    for i in range(r):
        for j in range(c):
            visited[i][j] = 0
            if graph[i][j] == 'S':
                queue.append((i, j))
                visited[i][j] = 1
                dist[i][j] = 0
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c: continue
            if visited[nx][ny] == 1: continue
            if water[nx][ny] != -1 and water[nx][ny] <= dist[x][y] + 1: continue
            if graph[nx][ny] == '.' or graph[nx][ny] == 'D':
                queue.append((nx, ny))
                visited[nx][ny] = 1
                dist[nx][ny] = dist[x][y] + 1

water_bfs()
bfs()

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'D':
            print(dist[i][j]) if dist[i][j] != -1 else print('KAKTUS')