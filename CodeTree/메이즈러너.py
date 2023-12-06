n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
maze = [[[] for _ in range(n)] for _ in range(n)]
participants = [[] for _ in range(m + 1)]

for i in range(1, m + 1):
    x, y = map(int, input().split())
    maze[x - 1][y - 1].append(i)
    participants[i].append(x - 1)
    participants[i].append(y - 1)

exit_x, exit_y = map(int, input().split())
exit_x -= 1
exit_y -= 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(num, x, y):
    global moving

    # 인접 4방향 최단 거리 구하기
    distance = [-1] * 4 # 상, 하, 좌, 우
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            distance[i] = abs(nx - exit_x) + abs(ny - exit_y)

    # 최단 거리가 더 가까운 칸으로 이동 (상하 우선)
    now_distance = abs(x - exit_x) + abs(y - exit_y)
    for i in range(4):
        if distance[i] != -1 and distance[i] <= now_distance:
            nx, ny = x + dx[i], y + dy[i]
            if nx == exit_x and ny == exit_y:
                participants[num] = []
                maze[x][y].remove(num)
                moving += 1
                break
            if graph[nx][ny] == 0:
                maze[nx][ny].append(num)
                maze[x][y].remove(num)
                participants[num][0], participants[num][1] = nx, ny
                moving += 1
                break

def find_square():
    candidates = []
    for i in range(1, m + 1):
        if participants[i]:
            x, y = participants[i][0], participants[i][1]
            row = abs(x - exit_x)
            column = abs(y - exit_y)
            d = max(row, column)
            r = min(x, exit_x)
            c = min(y, exit_y)
            if row > column:
                c = max(y, exit_y) - d
                while c < 0:
                    c += 1
                candidates.append((d, r, c))
            elif row < column:
                r = max(x, exit_x) - d
                while r < 0:
                    r += 1
                candidates.append((d, r, c))
            else:
                candidates.append((d, r, c))
    candidates.sort()
    return candidates[0]

def rotate():
    global exit_x, exit_y
    d, r, c = find_square()
    rotate_graph = [[0] * (d + 1) for _ in range(d + 1)]
    rotate_maze = [[[] for _ in range(d + 1)] for _ in range(d + 1)]
    for i in range(r, r + d + 1):
        for j in range(c, c + d + 1):
            rotate_graph[i - r][j - c] = graph[i][j]
            rotate_maze[i - r][j - c] = maze[i][j]
            if i == exit_x and j == exit_y:
                rotate_maze[i - r][j - c].append(-1)

    rotate_graph = list(map(list, zip(*rotate_graph[::-1])))
    rotate_maze = list(map(list, zip(*rotate_maze[::-1])))

    for i in range(r, r + d + 1):
        for j in range(c, c + d + 1):
            if rotate_graph[i - r][j - c] > 0:
                rotate_graph[i - r][j - c] -= 1
            graph[i][j] = rotate_graph[i - r][j - c]
            maze[i][j] = rotate_maze[i - r][j - c]
            if maze[i][j]:
                for v in maze[i][j]:
                    if v == -1:
                        exit_x, exit_y = i, j
                        maze[i][j].remove(-1)
                    else:
                        participants[v][0], participants[v][1] = i, j

moving = 0
for _ in range(k):
    # 이동
    for i in range(1, m + 1):
        if participants[i]:
            move(i, participants[i][0], participants[i][1])

    # 모두 탈출했는지 확인
    flag = all(not x for x in participants)
    if flag:
        break

    # 미로 회전
    rotate()

print(moving)
print(exit_x + 1, exit_y + 1)