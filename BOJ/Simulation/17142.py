from collections import deque

def bfs(active, b):
    queue = deque(active)
    visited = [[0] * n for _ in range(n)]
    for time, x, y in active:
        visited[x][y] = 1

    max_time = 0
    while queue:
        time, x, y = queue.popleft()
        if graph[x][y] == 0:
            max_time = max(max_time, time)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 1 and visited[nx][ny] == 0:
                if graph[nx][ny] == 0:
                    b -= 1
                queue.append((time + 1, nx, ny))
                visited[nx][ny] = 1

    if b:
        return -1
    else:
        return max_time

def dfs(depth, start, selected):
    if len(selected) == m:
        active = []
        for i in selected:
            active.append(virus[i])
        ans = bfs(active, blank)
        if ans != -1:
            answer.append(ans)
        return

    for i in range(start, len(virus) - m + 1 + depth):
        selected.append(i)
        dfs(depth + 1, i + 1, selected)
        selected.pop()

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

blank = 0
virus = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            blank += 1
        elif graph[i][j] == 2:
            virus.append((0, i, j))

answer = []
dfs(0, 0, [])
if answer:
    print(min(answer))
else:
    print(-1)