n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
chess = [[[] for _ in range(n)] for _ in range(n)]
horses = []
for i in range(k):
    x, y, d = map(int, input().split())
    horses.append([x - 1, y - 1, d - 1])
    chess[x - 1][y - 1].append(i)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def change_direction(d):
    if d == 0:
        return 1
    if d == 1:
        return 0
    if d == 2:
        return 3
    if d == 3:
        return 2

def move(num, x, y, d):
    nx, ny = x + dx[d], y + dy[d]
    # 범위 벗어나거나 이동하려는 칸이 파란색인 경우
    if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] == 2:
        d = change_direction(d)
        horses[num][2] = d
        nx, ny = x + dx[d], y + dy[d]

    # 이동
    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 2:
        idx = chess[x][y].index(num)
        for i in range(idx, len(chess[x][y])):
            horses[chess[x][y][i]][0] = nx
            horses[chess[x][y][i]][1] = ny

        if graph[nx][ny] == 0: # 다음 칸이 흰색
            chess[nx][ny].extend(chess[x][y][idx:])

        if graph[nx][ny] == 1: # 다음 칸이 빨간색
            chess[nx][ny].extend(chess[x][y][idx:][::-1])

        chess[x][y] = chess[x][y][:idx]

def check():
    for i in range(n):
        for j in range(n):
            if len(chess[i][j]) >= 4:
                return True
    return False

turn = 0
while True:
    if turn > 1000:
        turn = -1
        break

    turn += 1
    for i in range(k):
        x, y, d = horses[i]
        move(i, x, y, d)
        flag = 0
        if check():
            flag = 1
            break

    if flag == 1:
        break

print(turn)