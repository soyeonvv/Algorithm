n, m, x, y, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
d = list(map(int, input().split()))

# 동, 서, 북, 남
dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

dice = [0] * 6

for i in d:
    nx, ny = x + dr[i], y + dc[i]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    if i == 1: # 동
        dice[1], dice[3], dice[4], dice[5] = e, f, d, b
    elif i == 2: # 서
        dice[1], dice[3], dice[4], dice[5] = f, e, b, d
    elif i == 3: # 북
        dice[0], dice[1], dice[2], dice[3] = b, c, d, a
    else: # 남
        dice[0], dice[1], dice[2], dice[3] = d, a, b, c

    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[3]
    else:
        dice[3] = graph[nx][ny]
        graph[nx][ny] = 0

    x, y = nx, ny
    print(dice[1])