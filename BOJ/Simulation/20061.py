n = int(input())
graph = [[0] * 10 for _ in range(10)]

def place_blue(t, x):
    if t == 1:
        for i in range(6, 10):
            if graph[x][i] == 1:
                graph[x][i - 1] = 1
                break
            if i == 9:
                graph[x][i] = 1
    if t == 2:
        for i in range(6, 10):
            if graph[x][i] == 1:
                graph[x][i - 1] = 1
                graph[x][i - 2] = 1
                break
            if i == 9:
                graph[x][i] = 1
                graph[x][i - 1] = 1
    if t == 3:
        for i in range(6, 10):
            if graph[x][i] == 1 or graph[x + 1][i] == 1:
                graph[x][i - 1] = 1
                graph[x + 1][i - 1] = 1
                break
            if i == 9:
                graph[x][i] = 1
                graph[x + 1][i] = 1

def place_green(t, y):
    if t == 1:
        for i in range(6, 10):
            if graph[i][y] == 1:
                graph[i - 1][y] = 1
                break
            if i == 9:
                graph[i][y] = 1
    if t == 2:
        for i in range(6, 10):
            if graph[i][y] == 1 or graph[i][y + 1] == 1:
                graph[i - 1][y] = 1
                graph[i - 1][y + 1] = 1
                break
            if i == 9:
                graph[i][y] = 1
                graph[i][y + 1] = 1
    if t == 3:
        for i in range(6, 10):
            if graph[i][y] == 1:
                graph[i - 1][y] = 1
                graph[i - 2][y] = 1
                break
            if i == 9:
                graph[i][y] = 1
                graph[i - 1][y] = 1

def get_score():
    global score

    # 파란 영역
    for i in range(4, 10):
        block = 0
        for j in range(4):
            if graph[j][i] == 1:
                block += 1

        if block == 4:
            score += 1
            for y in range(i, 3, -1):
                for x in range(4):
                    graph[x][y] = graph[x][y - 1]
                    graph[x][y - 1] = 0

    # 초록 영역
    for i in range(4, 10):
        block = 0
        for j in range(4):
            if graph[i][j] == 1:
                block += 1

        if block == 4:
            score += 1
            for x in range(i, 3, -1):
                for y in range(4):
                    graph[x][y] = graph[x - 1][y]
                    graph[x - 1][y] = 0

def move_block():
    # 파란 영역
    flag1 = 0
    for i in range(4):
        if graph[i][4] == 1:
            flag1 += 1
            break
    for i in range(4):
        if graph[i][5] == 1:
            flag1 += 1
            break
    if flag1 != 0:
        for _ in range(flag1):
            for i in range(4):
                graph[i][9] = 0
            for i in range(9, 3, -1):
                for j in range(4):
                    graph[j][i] = graph[j][i - 1]
                    graph[j][i - 1] = 0

    # 초록 영역
    flag2 = 0
    for i in range(4):
        if graph[4][i] == 1:
            flag2 += 1
            break
    for i in range(4):
        if graph[5][i] == 1:
            flag2 += 1
            break
    if flag2 != 0:
        for _ in range(flag2):
            for i in range(4):
                graph[9][i] = 0
            for i in range(9, 3, -1):
                for j in range(4):
                    graph[i][j] = graph[i - 1][j]
                    graph[i - 1][j] = 0

score = 0
for _ in range(n):
    t, x, y = map(int, input().split())

    # 블록 놓기
    place_blue(t, x)
    place_green(t, y)

    # 점수 계산
    get_score()

    # 연한 칸에 블록 있는 경우
    move_block()

print(score)
cnt = 0
for i in range(10):
    for j in range(10):
        if graph[i][j] == 1:
            cnt += 1
print(cnt)