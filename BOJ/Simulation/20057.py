n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
x, y = n // 2, n // 2

# 좌 하 우 상
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

rate = [1, 1, 2, 2, 5, 7, 7, 10, 10]
windx = [
    # 좌
    [-1, 1, -2, 2, 0, -1, 1, -1, 1],
    # 하
    [-1, -1, 0, 0, 2, 0, 0, 1, 1],
    # 우
    [1, -1, 2, -2, 0, 1, -1, 1, -1],
    # 상
    [1, 1, 0, 0, -2, 0, 0, -1, -1]
]

windy = [
    # 좌
    [1, 1, 0, 0, -2, 0, 0, -1, -1],
    # 하
    [-1, 1, -2, 2, 0, -1, 1, -1, 1],
    # 우
    [-1, -1, 0, 0, 2, 0, 0, 1, 1],
    # 상
    [1, -1, 2, -2, 0, 1, -1, 1, -1]
]

def wind(x, y, d):
    value = 0
    sand = graph[x][y]
    sum_value = 0
    for i in range(9):
        nx, ny = x + windx[d][i], y + windy[d][i]
        r = (sand * rate[i]) // 100
        sum_value += r

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            value += r
            continue
        graph[nx][ny] += r

    # 알파
    nx, ny = x + dx[d], y + dy[d]
    a = sand - sum_value
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        value += a
    else:
        graph[nx][ny] += a

    graph[x][y] = 0
    return value

def solve(x, y):
    value = 0
    visited = [[False] * n for _ in range(n)]
    d = -1
    while True:
        if x == 0 and y == 0:
            break
        visited[x][y] = True
        nd = (d + 1) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]

        if visited[nx][ny]:
            nd = d
            nx = x + dx[nd]
            ny = y + dy[nd]

        value += wind(nx, ny, nd)
        x, y, d = nx, ny, nd

    return value

result = solve(x, y)
print(result)