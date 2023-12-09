from collections import deque

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]

N = int(input())
H = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == 'x':
            if bfs(nx, ny):
                gravity(nx, ny)

def bfs(x, y):
    queue = deque()
    visited = [[0] * C for _ in range(R)]
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        if x == R - 1:
            return False
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] == 'x' and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
    return True

def gravity(x, y):
    queue = deque()
    visited = [[0] * C for _ in range(R)]
    queue.append((x, y))
    visited[x][y] = 1
    cluster = []
    bottom = {}

    while queue:
        x, y = queue.popleft()
        cluster.append((x, y))
        bottom[y] = max(bottom.get(y, 0), x)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] == 'x' and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

    for y, x in bottom.items():
        for r in range(x + 1, R):
            if graph[r][y] == 'x':
                bottom[y] = r - x - 1
                break
        else:
            bottom[y] = R - x - 1

    d = min(bottom.values())
    for x, y in cluster:
        graph[x][y] = '.'
    for x, y in cluster:
        graph[x + d][y] = 'x'

for i in range(N):
    h = R - H[i]

    # 창영이가 왼쪽에서
    if i % 2 == 0:
        for j in range(C):
            if graph[h][j] == 'x':
                graph[h][j] = '.'
                check(h, j)
                break
    # 상근이가 오른쪽에서
    else:
        for j in range(C - 1, -1, -1):
            if graph[h][j] == 'x':
                graph[h][j] = '.'
                check(h, j)
                break

for row in graph:
    print(*row, sep='')