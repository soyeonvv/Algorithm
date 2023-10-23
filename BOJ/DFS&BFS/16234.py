from collections import deque

n, l, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] *  n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    temp = [(x, y)]
    sum_p = a[x][y]
    country = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx,  ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(a[nx][ny] - a[x][y]) <= r:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    temp.append((nx, ny))
                    sum_p += a[nx][ny]
                    country += 1
                    
    move = sum_p // country

    global flag
    if country > 1:
        flag = 1
        for i, j in temp:
            a[i][j] = move
    
while True:
    flag = 0
    visited = [[0] *  n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                bfs(i, j)

    if flag == 0:
        break

    answer += 1

print(answer)