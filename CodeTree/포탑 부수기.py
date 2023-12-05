from collections import deque

n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
attack = [[0] * m for _ in range(n)]
time = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def select_attacker():
    power = 5001
    ax = ay = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0: continue
            if graph[i][j] < power:
                power = graph[i][j]
                ax, ay = i, j
            elif graph[i][j] == power:
                if attack[i][j] > attack[ax][ay]:
                    ax, ay = i, j
                elif attack[i][j] == attack[ax][ay]:
                    if i + j > ax + ay:
                        ax, ay = i, j
                    elif i + j == ax + ay:
                        if j > ay:
                            ax, ay = i, j
    return ax, ay

def select_target(ax, ay):
    power = -1
    tx = ty = 0
    for i in range(n):
        for j in range(m):
            if i == ax and j == ay: continue
            if graph[i][j] == 0: continue
            if graph[i][j] > power:
                power = graph[i][j]
                tx, ty = i, j
            elif graph[i][j] == power:
                if attack[i][j] < attack[tx][ty]:
                    tx, ty = i, j
                elif attack[i][j] == attack[tx][ty]:
                    if i + j < tx + ty:
                        tx, ty = i, j
                    elif i + j == tx + ty:
                        if j < ty:
                            tx, ty = i, j
    return tx, ty

def laser_attack(ax, ay, tx, ty):
    queue = deque()
    visited = [[0] * m for _ in range(n)]
    queue.append((ax, ay, []))
    visited[ax][ay] = 1

    while queue:
        x, y, route = queue.popleft()
        for i in range(4):
            nx, ny = (x + dx[i]) % n, (y + dy[i]) % m

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and graph[nx][ny] != 0:
                    if (nx, ny) == (tx, ty):
                        for rx, ry in route:
                            graph[rx][ry] -= graph[ax][ay] // 2
                            check[rx][ry] = 1
                        return False

                    temp = route[:]
                    temp.append((nx, ny))
                    queue.append((nx, ny, temp))
                    visited[nx][ny] = 1
    return True

def turret_attack(ax, ay, tx, ty):
    ddx = dx + [-1, 1, 1, -1]
    ddy = dy + [1, 1, -1, -1]
    for i in range(8):
        nx, ny = (tx + ddx[i]) % n, (ty + ddy[i]) % m
        if nx == ax and ny == ay:
            continue
        graph[nx][ny] -= graph[ax][ay] // 2
        check[nx][ny] = 1

for _ in range(k):
    check = [[0] * m for _ in range(n)]

    # 공격자 선정
    attacker_x, attacker_y = select_attacker()
    graph[attacker_x][attacker_y] += (n + m)
    check[attacker_x][attacker_y] = 1
    attack[attacker_x][attacker_y] = time
    time += 1

    # 공격대상 선정
    target_x, target_y = select_target(attacker_x, attacker_y)
    graph[target_x][target_y] -= graph[attacker_x][attacker_y]
    check[target_x][target_y] = 1

    # 레이저 공격
    if laser_attack(attacker_x, attacker_y, target_x, target_y):
        # 포탑 공격
        turret_attack(attacker_x, attacker_y, target_x, target_y)

    # 포탑 부서짐
    for i in range(n):
        for j in range(m):
            if graph[i][j] < 0:
                graph[i][j] = 0

    # 포탑 정비
    if sum(i.count(0) for i in graph) == (n * m - 1):
        break
    for i in range(n):
        for j in range(m):
            if check[i][j] != 1 and graph[i][j] != 0:
                graph[i][j] += 1

answer = max(max(i) for i in graph)
print(answer)