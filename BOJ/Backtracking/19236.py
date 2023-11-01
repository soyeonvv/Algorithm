import copy

def find_fish(num, graph):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == num:
                return (i, j)

def move_fish(graph):
    # 물고기가 1번부터 번호 순서대로 이동
    for i in range(1, 17):
        fish_pos = find_fish(i, graph)
        if not fish_pos:
            continue
        x, y = fish_pos[0], fish_pos[1]
        for direction in range(8):
            d = (graph[x][y][1] + direction) % 8
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if graph[nx][ny][0] != -1:
                    graph[x][y][1] = d
                    graph[nx][ny], graph[x][y] = graph[x][y], graph[nx][ny]
                    break

def move_shark(x, y, graph):
    shark_d = graph[x][y][1]
    position = []
    for _ in range(3):
        x += dx[shark_d]
        y += dy[shark_d]
        if 0 <= x < 4 and 0 <= y < 4 and graph[x][y][0] != 0:
            position.append((x, y))
    return position

def dfs(shark_x, shark_y, eat, graph):
    global answer
    graph = copy.deepcopy(graph)

    eat += graph[shark_x][shark_y][0]
    graph[shark_x][shark_y][0] = -1

    move_fish(graph)
    position = move_shark(shark_x, shark_y, graph)

    if position:
        for sx, sy in position:
            graph[shark_x][shark_y][0] = 0
            dfs(sx, sy, eat, graph)
            graph[shark_x][shark_y][0] = -1
    else:
        answer = max(answer, eat)
        return

graph = [[[], [], [], []] for _ in range(4)]

for i in range(4):
    value = list(map(int, input().split()))
    for j in range(8):
        if j % 2 != 0:
            graph[i][j // 2].append(value[j] - 1)
        else:
            graph[i][j // 2].append(value[j])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 상어가 (0, 0) 물고기 먹고 물고기 방향을 가짐
shark_x, shark_y = 0, 0
answer = 0

dfs(shark_x, shark_y, 0, graph)
print(answer)