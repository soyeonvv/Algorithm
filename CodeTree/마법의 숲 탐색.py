from collections import deque

r, c, k = map(int, input().split())
spirit = [list(map(int, input().split())) for _ in range(k)]
graph = [[0] * c for _ in range(r + 3)]
exit_pos = [[] for _ in range(k + 1)]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 남, 서남, 동남
mx = [1, 1, 1]
my = [0, -1, 1]

def move_golem(cx, cy, d, ed, golem, idx):
    for i, (x, y) in enumerate(golem):
        graph[x][y] = 0
        golem[i][0], golem[i][1] = x + mx[d], y + my[d]
        # 출구 좌표 업데이트
        if [x, y] == exit_pos[idx]:
            exit_pos[idx][0], exit_pos[idx][1] = golem[i][0], golem[i][1]

    # 출구 회전
    if ed != -1:
        ex, ey = cx + dx[ed], cy + dy[ed]
        for i, (x, y) in enumerate(golem):
            if x == ex and y == ey:
                exit_pos[idx][0], exit_pos[idx][1] = ex, ey

    for x, y in golem:
        graph[x][y] = idx

def move_down(cx, cy, d, golem, idx):
    move_golem(cx + 1, cy, 0, -1, golem, idx)
    return cx + 1, cy, d

def move_diagonal(cx, cy, d, golem, idx, direction):
    v = -1 if direction == 'west' else 1
    dd = 1 if direction == 'west' else 2
    
    # 출구 방향 변경
    ed = (d + v) % 4
    move_golem(cx + 1, cy + v, dd, ed, golem, idx)

    return cx + 1, cy + v, ed

def goDown(x, y, new_graph):
    if x + 1 < r + 3:
        if new_graph[x][y - 1] == 0 and new_graph[x + 1][y] == 0 and new_graph[x][y + 1] == 0:
            return True
    return False

def goDiagonal(x, y, direction):
    d = -1 if direction == 'west' else 1

    if 0 <= y + d < c:
        if graph[x - 1][y] == 0 and graph[x][y + d] == 0 and graph[x + 1][y] == 0:
            new_graph = [row[:] for row in graph]
            new_graph[x][y], new_graph[x][y - d] = 0, 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                new_graph[nx][ny], new_graph[nx][ny - d] = 0, 0
            if goDown(x + 1, y, new_graph):
                return True
    return False

def move(x, y, d, golem, idx):
    # 남쪽 이동
    if goDown(x + 1, y, graph):
        return move_down(x, y, d, golem, idx)
    # 서남 이동
    elif goDiagonal(x, y - 1, 'west'):
        return move_diagonal(x, y, d, golem, idx, 'west')
    # 동남 이동
    elif goDiagonal(x, y + 1, 'east'):
        return move_diagonal(x, y, d, golem, idx, 'east')
    else:
        return -1

def bfs(x, y):
    result = x
    queue = deque()
    visited = [[0] * c for _ in range(r + 3)]
    visited[x][y] = 1
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 1. 범위 내에 있고 2. 같은 골렘 내부에 있거나(idx 동일) 3. 출구에서 다른 골렘 이동
            if 0 <= nx < r + 3 and 0 <= ny < c and visited[nx][ny] == 0:
                if graph[x][y] == graph[nx][ny] or ([x, y] == exit_pos[graph[x][y]] and graph[nx][ny] != 0):
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    result = max(result, nx)

    return result - 2

def move_spirit(cx, cy):
    global graph, answer
    # 골렘의 일부가 숲을 벗어난 경우
    if cx <= 3:
        graph = [[0] * c for _ in range(r + 3)]
        return

    # 정령 이동
    answer += bfs(cx, cy)

answer = 0
idx = 1
for col, d in spirit:
    golem = []
    # 골렘 중심
    x, y = 1, col - 1
    # 지도에 골렘 표시
    graph[x][y] = idx
    golem.append([x, y])
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        graph[nx][ny] = idx
        golem.append([nx, ny])
        if i == d:
            exit_pos[idx].append(nx)
            exit_pos[idx].append(ny)

    while True:
        value = move(x, y, d, golem, idx)
        if value == -1:
            move_spirit(x, y)
            break
        else:
            x, y, d = value

    idx += 1

print(answer)