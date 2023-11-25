from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
num = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = num
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and graph[nx][ny] != 0:
                queue.append((nx, ny))
                graph[nx][ny] = num
                visited[nx][ny] = 1

def distance(number):
    queue = deque()
    dist = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == number:
                dist[i][j] = 0
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] != 0 and graph[nx][ny] != number:
                    return dist[x][y]
                elif graph[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

    return int(1e9)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)
            num += 1

answer = int(1e9)
for i in range(1, num):
    answer = min(answer, distance(i))

print(answer)