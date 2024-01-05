n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
people = []

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

flag = 0
def find_member(team, x, y):
    global flag
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            if graph[x][y] == 1 and graph[nx][ny] == 2 or graph[x][y] != 1 and graph[nx][ny] not in [0, 4]:
                team.append([nx, ny])
                visited[nx][ny] = 1
                if graph[nx][ny] == 3:
                    flag = 1
                    return team
                find_member(team, nx, ny)
                if flag:
                    return team

visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            visited[i][j] = 1
            team = find_member([[i, j]], i, j)
            people.append(team)

def move():
    t_num = 0
    for team in people:
        num = 0
        for x, y in team:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if num == 0:
                        if graph[nx][ny] == 4 or graph[nx][ny] == 3:
                            people[t_num][num][0], people[t_num][num][1] = nx, ny
                            graph[nx][ny] = graph[x][y]
                            graph[x][y] = -1
                            break
                    elif num == len(people[t_num]) - 1:
                        if graph[nx][ny] == -1:
                            people[t_num][num][0], people[t_num][num][1] = nx, ny
                            graph[nx][ny] = 3
                            if graph[x][y] == 3:
                                graph[x][y] = 4
                            break
                    else:
                        if graph[nx][ny] == -1:
                            people[t_num][num][0], people[t_num][num][1] = nx, ny
                            graph[nx][ny] = graph[x][y]
                            if graph[nx][ny] == 3:
                                graph[x][y] = 4
                            else:
                                graph[x][y] = -1
                            break
            num += 1
        t_num += 1

def turn(num):
    people[num].reverse()
    i = 0
    for x, y in people[num]:
        if i == 0:
            graph[x][y] = 1
        elif i == len(people[num]) - 1:
            graph[x][y] = 3
        else:
            graph[x][y] = 2
        i += 1

def get_score(x, y):
    global answer
    for i, team in enumerate(people):
        if [x, y] in team:
            j = team.index([x, y])
            break
    answer += (j + 1) ** 2
    turn(i)

def ball_move(a, b, c, d, num):
    for i in range(a, b, c):
        if d == 0:
            if graph[num][i] in [1, 2, 3]:
                get_score(num, i)
                break
        else:
            if graph[i][num] in [1, 2, 3]:
                get_score(i, num)
                break

def ball(r):
    d = r // n % 4
    if r % n == 0:
        d = (r // n - 1) % 4
    if d == 0 or d == 1:
        num = r % n - 1
        if num == -1:
            num = n - 1
    else:
        num = n - r % n
        if num == n:
            num = 0

    if d == 0:
        ball_move(0, n, 1, 0, num)
    elif d == 1:
        ball_move(n - 1, -1, -1, 1, num)
    elif d == 2:
        ball_move(n - 1, -1, -1, 0, num)
    else:
        ball_move(0, n, 1, 1, num)

answer = 0
for r in range(1, k + 1):
    # 각 팀 이동
    move()
    # 공 던지기
    ball(r)

print(answer)