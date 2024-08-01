n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
candidates = []
answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check_range(x, y, size):
    if x - size >= 0 and x + size < n and y - size >= 0 and y + size < m:
        return True
    return False

def search(x, y):
    size = 0
    while check_range(x, y, size) and graph[x - size][y] == graph[x + size][y] == graph[x][y - size] == graph[x][y + size] == '#':
        size += 1
        candidates.append((x, y, size))

def check(a, b):
    ax, ay, sizeA = a
    bx, by, sizeB = b
    board = [[0] * m for _ in range(n)]

    board[ax][ay], board[bx][by] = 1, 1
    for i in range(1, sizeA):
        for d in range(4):
            nx, ny = ax + dx[d] * i, ay + dy[d] * i
            board[nx][ny] = 1
    for i in range(1, sizeB):
        for d in range(4):
            nx, ny = bx + dx[d] * i, by + dy[d] * i
            if board[nx][ny] == 1:
                return False

    return True


for i in range(n):
    for j in range(m):
        if graph[i][j] == '#':
            search(i, j)

for i in range(len(candidates) - 1):
    for j in range(i + 1, len(candidates)):
        result = ((candidates[i][2] - 1) * 4 + 1) * ((candidates[j][2] - 1) * 4 + 1)
        if result > answer and check(candidates[i], candidates[j]):
            answer = result

print(answer)