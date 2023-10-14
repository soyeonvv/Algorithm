from collections import deque

# 벽 체크
def up_check(i, j, k):
    if wall_hor[i][j] == 1:
        return False
    if not (0 <= i + dx[k] < r and 0 <= j + dy[k] < c):
        return False
    return True

def down_check(i, j, k):
    if 0 <= i + dx[k] < r and 0 <= j + dy[k] < c:
        if wall_hor[i + dx[k]][j + dy[k]] == 0:
            return True
    return False

def right_check(i, j, k):
    if wall_ver[i][j] == 1:
        return False
    if not (0 <= i + dx[k] < r and 0 <= j + dy[k] < c):
        return False
    return True

def left_check(i, j, k):
    if 0 <= i + dx[k] < r and 0 <= j + dy[k] < c:
        if wall_ver[i + dx[k]][j + dy[k]] == 0:
            return True
    return False

def wind():
    fan = []
    for i in range(r):
        for j in range(c):
            if 1 <= graph[i][j] <= 4:
                fan.append((i, j, graph[i][j] - 1))

    for x, y, d in fan:
        temp = [[0] * c for _ in range(r)]
        x, y = x + dx[d], y + dy[d]
        temp[x][y] = 5

        q = deque()
        q.append((x, y, 5))
        while q:
            px, py, t = q.popleft()

            if t == 0:
                break
            if d == 0: # 북동, 동, 남동으로 바람 붐
                if up_check(px, py, 2):
                    if right_check(px - 1, py, 0):
                        q.append((px - 1, py + 1, t - 1))
                        temp[px - 1][py + 1] = t - 1
                if right_check(px, py, 0):
                    q.append((px, py + 1, t - 1))
                    temp[px][py + 1] = t - 1
                if down_check(px, py, 3):
                    if right_check(px + 1, py, 0):
                        q.append((px + 1, py + 1, t - 1))
                        temp[px + 1][py + 1] = t - 1

            elif d == 1: # 북서, 서, 남서
                if up_check(px, py, 2):
                    if left_check(px - 1, py, 1):
                        q.append((px - 1, py - 1, t - 1))
                        temp[px - 1][py - 1] = t - 1
                if left_check(px, py, 1):
                    q.append((px, py - 1, t - 1))
                    temp[px][py - 1] = t - 1
                if down_check(px, py, 3):
                    if left_check(px + 1, py, 1):
                        q.append((px + 1, py - 1, t - 1))
                        temp[px + 1][py - 1] = t - 1

            elif d == 2:  # 북서, 북, 북동
                if left_check(px, py, 1):
                    if up_check(px, py - 1, 2):
                        q.append((px - 1, py - 1, t - 1))
                        temp[px - 1][py - 1] = t - 1
                if up_check(px, py, 2):
                    q.append((px - 1, py, t - 1))
                    temp[px - 1][py] = t - 1
                if right_check(px, py, 0):
                    if up_check(px, py + 1, 2):
                        q.append((px - 1, py + 1, t - 1))
                        temp[px - 1][py + 1] = t - 1

            elif d == 3:  # 남서, 남, 남동
                if left_check(px, py, 1):
                    if down_check(px, py - 1, 3):
                        q.append((px + 1, py - 1, t - 1))
                        temp[px + 1][py - 1] = t - 1
                if down_check(px, py, 3):
                    q.append((px + 1, py, t - 1))
                    temp[px + 1][py] = t - 1
                if right_check(px, py, 0):
                    if down_check(px, py + 1, 3):
                        q.append((px + 1, py + 1, t - 1))
                        temp[px + 1][py + 1] = t - 1

        for i in range(r):
            for j in range(c):
                temperature[i][j] += temp[i][j]

def change_temperature(i, j, t):
    global change_temp
    x, y = i + dx[t], j + dy[t]
    value = abs(temperature[i][j] - temperature[x][y]) // 4

    if temperature[i][j] > temperature[x][y]:
        change_temp[i][j] -= value
    elif temperature[i][j] < temperature[x][y]:
        change_temp[i][j] += value

def change():
    global change_temp
    change_temp = [i[:] for i in temperature]

    for i in range(r):
        for j in range(c):
            if right_check(i, j, 0):
                change_temperature(i, j, 0)
            if left_check(i, j, 1):
                change_temperature(i, j, 1)
            if up_check(i, j, 2):
                change_temperature(i, j, 2)
            if down_check(i, j, 3):
                change_temperature(i, j, 3)

    return change_temp

def temp_down():
    for i in range(r):
        for j in range(c):
            cnt = 0
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if not (0 <= x < r and 0 <= y < c):
                    cnt += 1
            if cnt != 0:
                if temperature[i][j] > 0:
                    temperature[i][j] -= 1

def test_success():
    for tx, ty in test:
        if temperature[tx][ty] < k:
            return False
    return True

r, c, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
temperature = [[0] * c for _ in range(r)]
w = int(input())
wall_hor = [[0] * c for _ in range(r)] # 위 아래에 벽
wall_ver = [[0] * c for _ in range(r)] # 양 옆 사이에 벽
for _ in range(w):
    x, y, t = map(int, input().split())
    x -= 1
    y -= 1
    if t == 0:
        wall_hor[x][y] = 1
    elif t == 1:
        wall_ver[x][y] = 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 조사할 곳 좌표
test = []
for i in range(r):
    for j in range(c):
        if graph[i][j] == 5:
            test.append((i, j))

chocolate = 0
while True:
    # 온풍기 바람 나옴
    wind()
    # 온도 조절
    temperature = change()
    # 바깥 쪽 온도 감소
    temp_down()
    # 초콜릿 먹음
    chocolate += 1
    if test_success():
        break
    if chocolate > 100:
        chocolate = 101
        break

print(chocolate)