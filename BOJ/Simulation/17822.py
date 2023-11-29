from collections import deque

n, m, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(num, d, k):
    v = k % m
    # 시계 방향
    if d == 0:
        graph[num] = graph[num][m - v:] + graph[num][:m - v]
    # 반시계 방향
    if d == 1:
        graph[num] = graph[num][v:] + graph[num][:v]

def bfs(x, y):
    queue = deque()
    z = graph[x][y]
    flag = 0

    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if ny == -1:
                ny = m - 1
            elif ny == m:
                ny = 0
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and graph[nx][ny] == z:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    graph[x][y] = 'x'
                    graph[nx][ny] = 'x'
                    flag = 1

    return flag

def calculate():
    cnt, value = 0, 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 'x':
                cnt += 1
                value += graph[i][j]

    if cnt > 0:
        value /= cnt
        for i in range(n):
            for j in range(m):
                if graph[i][j] != 'x':
                    if float(graph[i][j]) > value:
                        graph[i][j] -= 1
                    elif float(graph[i][j]) < value:
                        graph[i][j] += 1

def change():
    flag = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 'x' and visited[i][j] != 1:
                flag += bfs(i, j)

    if flag == 0:
        calculate()

for _ in range(t):
    x, d, k = map(int, input().split())

    # x배수의 원판 d방향으로 k칸 이동
    for i in range(1, n + 1):
        if i % x == 0:
            move(i - 1, d, k)

    visited = [[0] * m for _ in range(n)]
    change()

answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] != 'x':
            answer += graph[i][j]
print(answer)