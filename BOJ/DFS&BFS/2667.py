from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
answer = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    graph[i][j] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                cnt += 1
    answer.append(cnt)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i, j)

answer.sort()
print(len(answer))
for i in answer:
    print(i)