import heapq

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
sx, sy = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            sx, sy = i, j
            break

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check_nearG(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 'g':
            return 1
    return 0

q = []
visited = [[0] * m for _ in range(n)]
heapq.heappush(q, (0, 0, sx, sy))
visited[sx][sy] = 1

while q:
    a, b, x, y = heapq.heappop(q)
    if graph[x][y] == 'F':
        print(a, b)
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            if graph[nx][ny] == 'g':
                heapq.heappush(q, (a + 1, b, nx, ny))
            elif graph[nx][ny] == '.':
                heapq.heappush(q, (a, b + check_nearG(nx, ny), nx, ny))
            else:
                heapq.heappush(q, (a, b, nx, ny))
            visited[nx][ny] = 1