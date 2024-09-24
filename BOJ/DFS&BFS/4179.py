from collections import deque

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
visited_J = [[0] * c for _ in range(r)]
visited_F = [[0] * c for _ in range(r)]

queue_J = deque()
queue_F = deque()

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            queue_J.append((i, j))
            visited_J[i][j] = 1
        elif graph[i][j] == 'F':
            queue_F.append((i, j))
            visited_F[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue_F:
        x, y = queue_F.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != '#' and visited_F[nx][ny] == 0:
                visited_F[nx][ny] = visited_F[x][y] + 1
                queue_F.append((nx, ny))

    while queue_J:
        x, y = queue_J.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] != '#' and visited_J[nx][ny] == 0:
                    if visited_F[nx][ny] == 0 or visited_F[nx][ny] > visited_J[x][y] + 1:
                        visited_J[nx][ny] = visited_J[x][y] + 1
                        queue_J.append((nx, ny))
            else:
                return visited_J[x][y]

    return 'IMPOSSIBLE'

print(bfs())