def check(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        while 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 'O':
            if graph[nx][ny] == 'S':
                return False
            else:
                nx += dx[i]
                ny += dy[i]
    return True

def dfs(cnt):
    global answer
    if cnt == 3:
        teacher, c = 0, 0
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'T':
                    teacher += 1
                    if check(i, j):
                        c += 1
        if c == teacher:
            answer = -1
        return

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                dfs(cnt + 1)
                graph[i][j] = 'X'

n = int(input())
graph = [list(input().split()) for _ in range(n)]
answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dfs(0)

if answer == -1:
    print('YES')
else:
    print('NO')