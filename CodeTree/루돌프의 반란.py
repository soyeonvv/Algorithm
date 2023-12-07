from collections import deque

n, m, p, C, D = map(int, input().split())
rudolf_x, rudolf_y = map(int, input().split())
rudolf_x -= 1
rudolf_y -= 1
graph = [[-1] * n for _ in range(n)]
santa = []
santa_check = [0] * p
for _ in range(p):
    num, x, y = map(int, input().split())
    graph[x - 1][y - 1] = num - 1
    santa.append([x - 1, y - 1, 0, num - 1])
santa.sort(key=lambda x:x[3])
score = [0] * p

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def interaction(sx, sy, nx, ny, d, f):
    queue = deque()
    queue.append((nx, ny))
    value = graph[sx][sy]
    graph[sx][sy] = -1
    santa[value][0], santa[value][1] = nx, ny

    while queue:
        x, y = queue.popleft()
        v = graph[x][y]
        graph[x][y] = value
        if f == 'r':
            n_x, n_y = x + d[0], y + d[1]
        elif f == 's':
            n_x, n_y = x - d[0], y - d[1]
        if n_x < 0 or n_x >= n or n_y < 0 or n_y >= n:
            santa_check[v] = 1
            break
        else:
            santa[v][0], santa[v][1] = n_x, n_y
            if graph[n_x][n_y] == -1:
                graph[n_x][n_y] = v
                break
            else:
                queue.append((n_x, n_y))
                value = v

def crash(num, s, d, f, T):
    score[num] += s
    sx, sy = santa[num][0], santa[num][1]
    if f == 'r':
        nx, ny = rudolf_x + (d[0] * s), rudolf_y + (d[1] * s)
    elif f == 's':
        nx, ny = rudolf_x - (d[0] * s), rudolf_y - (d[1] * s)
    # 산타 탈락
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        santa_check[num] = 1
        graph[sx][sy] = -1
        return
    # 상호작용
    if graph[nx][ny] != -1 and graph[nx][ny] != num:
        interaction(sx, sy, nx, ny, d, f)

    graph[sx][sy] = -1
    graph[nx][ny] = num
    santa[num][0], santa[num][1] = nx, ny
    # 산타 기절
    santa[num][2] = T + 1

def move_rudolf(T):
    global rudolf_x, rudolf_y
    x = [10000, 10000, 0]
    for sx, sy, i, sn in santa:
        if santa_check[sn] == 1:
            continue
        v = [(rudolf_x - sx) ** 2 + (rudolf_y - sy) ** 2, -sx, -sy]
        if x > v:
            x = v

    # 산타가 있는 방향으로 한칸 돌진
    sx, sy, d_x, d_y = -x[1], -x[2], 0, 0
    if rudolf_x < sx:
        rudolf_x += 1
        d_x += 1
    elif rudolf_x > sx:
        rudolf_x -= 1
        d_x -= 1
    if rudolf_y < sy:
        rudolf_y += 1
        d_y +=1
    elif rudolf_y > sy:
        rudolf_y -= 1
        d_y -= 1

    # 루돌프가 이동한 칸에 산타 있으면 충돌
    if graph[rudolf_x][rudolf_y] != -1:
        crash(graph[rudolf_x][rudolf_y], C, (d_x, d_y), 'r', T)

def move_santa(T):
    for sx, sy, t, sn in santa:
        if t < T and santa_check[sn] != 1:
            distance = [-1] * 4
            for d in range(4):
                nx, ny = sx + dx[d], sy + dy[d]
                if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] != -1:
                    continue
                distance[d] = (rudolf_x - nx) ** 2 + (rudolf_y - ny) ** 2
            now = (rudolf_x - sx) ** 2 + (rudolf_y - sy) ** 2

            if distance.count(-1) == 4 or all(x > now for x in distance if x != -1):
                continue
            else:
                min_value = min(x for x in distance if x != -1)
                for j in range(len(distance)):
                    if distance[j] == min_value:
                        nx, ny = sx + dx[j], sy + dy[j]
                        direction = j
                        break
                # 산타가 이동한 칸에 루돌프가 있으면 충돌
                if nx == rudolf_x and ny == rudolf_y:
                    crash(sn, D, (dx[direction], dy[direction]), 's', T)
                else:
                    graph[nx][ny] = sn
                    santa[sn][0], santa[sn][1] = nx, ny
                    graph[sx][sy] = -1

for T in range(1, m + 1):
    if santa_check.count(1) == p:
        break
    # 루돌프 이동
    move_rudolf(T)
    # 산타 이동
    move_santa(T)
    # 살아남은 산타 점수
    for i in range(p):
        if santa_check[i] == 0:
            score[i] += 1

for i in score:
    print(i, end=' ')