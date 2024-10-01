from collections import deque

n, m = map(int, input().split())
graph = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, a, b = map(int, input().split())
    graph[x - 1][y - 1].append((a - 1, b - 1))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
visited = [[0] * n for _ in range(n)]
queue.append((0, 0))
visited[0][0] = 1

light = [[0] * n for _ in range(n)]
light[0][0] = 1

for a, b in graph[0][0]:
    light[a][b] = 1

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and light[nx][ny] == 1:
            visited[nx][ny] = 1
            queue.append((nx, ny))
            for a, b in graph[nx][ny]:
                light[a][b] = 1

                for i in range(4):
                    na, nb = a + dx[i], b + dy[i]
                    if 0 <= na < n and 0 <= nb < n and visited[na][nb] == 1 and light[na][nb] == 1:
                        queue.append((na, nb))

answer = 0
for i in range(n):
    for j in range(n):
        if light[i][j] == 1:
            answer += 1

print(answer)