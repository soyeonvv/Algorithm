R, C, M = map(int, input().split())
graph = [[0] * C for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    graph[r - 1][c - 1] = (s, d - 1, z)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def direction(d):
    if d == 0: return 1
    elif d == 1: return 0
    elif d == 2: return 3
    else: return 2

def move(x, y, s, d):
    if d == 0 or d == 1:
        s = s % ((R - 1) * 2)
    else:
        s = s % ((C - 1) * 2)

    nx, ny = x, y
    for _ in range(s):
        nx += dx[d]
        ny += dy[d]
        if 0 <= nx < R and 0 <= ny < C:
            continue
        else:
            nx -= dx[d]
            ny -= dy[d]
            d = direction(d)
            nx += dx[d]
            ny += dy[d]
    return nx, ny, d

def move_shark():
    move_graph = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j] != 0:
                s, d, z = graph[i][j]
                nx, ny, d = move(i, j, s, d)
                if move_graph[nx][ny] == 0:
                    move_graph[nx][ny] = (s, d, z)
                else:
                    if move_graph[nx][ny][2] < graph[i][j][2]:
                        move_graph[nx][ny] = (s, d, z)
    return move_graph

fisherman = -1
answer = 0
while True:
    # 낚시왕 오른쪽으로 한 칸 이동
    fisherman += 1
    if fisherman == C:
        break

    # 낚시
    for i in range(R):
        if graph[i][fisherman] != 0:
            answer += graph[i][fisherman][2]
            graph[i][fisherman] = 0
            break

    # 상어 이동
    graph = move_shark()

print(answer)