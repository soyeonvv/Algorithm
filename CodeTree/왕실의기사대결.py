from collections import deque

l, n, q = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(l)]
robot = [[0] * l for _ in range(l)]
robot_info = [[]]
stats = [0]
damage = [0] * (n + 1)
for i in range(1, n + 1):
    r, c, h, w, k = map(int, input().split())
    for x in range(r - 1, r - 1 + h):
        for y in range(c - 1, c - 1 + w):
            robot[x][y] = i
    robot_info.append([r - 1, c - 1, h, w])
    stats.append(k)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def get_move_robot(num, d):
    x, y = robot_info[num][0], robot_info[num][1]
    queue = deque()
    visited = [[0] * l for _ in range(l)]
    queue.append((x, y))
    visited[x][y] = 1
    move_robot = [num]

    flag = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < l and 0 <= ny < l:
                if robot[x][y] == robot[nx][ny] and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
            if i == d:
                if 0 <= nx < l and 0 <= ny < l:
                    if robot[nx][ny] > 0 and robot[x][y] != robot[nx][ny] and visited[nx][ny] == 0:
                        queue.append((nx, ny))
                        visited[nx][ny] = 1
                        move_robot.append(robot[nx][ny])
                    if graph[nx][ny] == 2:
                        flag = 1
                        break
                else:
                    flag = 1
                    break
        if flag:
            return flag, move_robot

    return flag, move_robot

def move(lst, d):
    temp = [[0] * l for _ in range(l)]
    for i in lst:
        r, c, h, w = robot_info[i]
        robot_info[i][0], robot_info[i][1] = r + dx[d], c + dy[d]
        for x in range(r, r + h):
            for y in range(c, c + w):
                nx, ny = x + dx[d], y + dy[d]
                temp[nx][ny] = i
    for i in range(l):
        for j in range(l):
            if robot[i][j] > 0 and temp[i][j] == 0:
                if robot[i][j] in lst:
                    robot[i][j] = 0
            if temp[i][j] > 0:
                robot[i][j] = temp[i][j]

def get_damage(num, lst):
    for i in range(l):
        for j in range(l):
            if robot[i][j] > 0 and graph[i][j] == 1:
                if robot[i][j] in lst and robot[i][j] != num:
                    if stats[robot[i][j]] != 0:
                        stats[robot[i][j]] -= 1
                        damage[robot[i][j]] += 1
                        if stats[robot[i][j]] == 0:
                            damage[robot[i][j]] = 0
                            r, c, h, w = robot_info[robot[i][j]]
                            for x in range(r, r + h):
                                for y in range(c, c + w):
                                    robot[x][y] = 0
                            continue

for _ in range(q):
    num, d = map(int, input().split())
    if stats[num] == 0:
        continue

    # 움직일 로봇 리스트
    f, lst = get_move_robot(num, d)

    if f == 0:
        lst = list(set(lst))
        # 로봇 이동
        move(lst, d)
        # 데미지
        get_damage(num, lst)

print(sum(damage))