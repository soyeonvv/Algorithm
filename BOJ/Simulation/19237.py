n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
shark_direction = [0] + list(map(int, input().split()))

priority = [[] for _ in range(m + 1)]
for i in range(1, m + 1):
    for j in range(4):
        priority[i].append(list(map(int, input().split())))

smell = [[[0, 0]] * n for _ in range(n)]
time = 0

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

def move():
    move_graph = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if graph[x][y] != 0:
                d = shark_direction[graph[x][y]] - 1
                flag = False
                for i in priority[graph[x][y]][d]:
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][1] == 0:
                            shark_direction[graph[x][y]] = i
                            if move_graph[nx][ny] == 0:
                                move_graph[nx][ny] = graph[x][y]
                            else:
                                move_graph[nx][ny] = min(move_graph[nx][ny], graph[x][y])
                            flag = True
                            break
                if flag:
                    continue
                for i in priority[graph[x][y]][d]:
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][0] == graph[x][y]:
                            shark_direction[graph[x][y]] = i
                            move_graph[nx][ny] = graph[x][y]
                            break
    return move_graph

while True:
    time += 1

    # 상어가 자신의 위치에 냄새를 뿌린다.
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if graph[i][j] != 0:
                smell[i][j] = [graph[i][j], k]

    # 상어 이동
    graph = move()

    check = True
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 1:
                check = False
    if check:
        break

    if time >= 1000:
        time = -1
        break

print(time)