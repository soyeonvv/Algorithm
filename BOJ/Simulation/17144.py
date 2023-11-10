from collections import deque

r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

up, down = 0, 0
for i in range(r):
    if graph[i][0] == -1:
        up, down = i, i + 1
        break

# 동 북 서 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def clean_up():
    d = 0
    x, y = up, 1
    before = 0
    while True:
        nx, ny = x + dx[d], y + dy[d]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            d += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x, y = nx, ny

def clean_down():
    d = 0
    x, y = down, 1
    before = 0
    while True:
        nx, ny = x + dx[d], y + dy[d]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            d -= 1
            continue
        graph[x][y], before = before, graph[x][y]
        x, y = nx, ny

for _ in range(t):
    queue = deque()
    dust = [[0] * c for _ in range(r)]

    # 미세먼지 확산
    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        cnt = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                dust[nx][ny] += graph[x][y] // 5
                cnt += 1
        dust[x][y] -= (graph[x][y] // 5) * cnt
    for i in range(r):
        for j in range(c):
            graph[i][j] += dust[i][j]

    # 공기청정기 작동
    clean_up()
    clean_down()

# 미세먼지 카운트
answer = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] > 0:
            answer += graph[i][j]

print(answer)