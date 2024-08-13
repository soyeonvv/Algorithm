from collections import deque

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
water_q, water_temp, swan_q, swan_temp = deque(), deque(), deque(), deque()
water_visited = [[0] * c for _ in range(r)]
swan_visited = [[0] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'L':
            if not swan_q:
                swan_q.append((i, j))
                swan_visited[i][j] = 1
            else:
                sx, sy = i, j
            water_q.append((i, j))
            water_visited[i][j] = 1
        elif graph[i][j] == '.':
            water_q.append((i, j))
            water_visited[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check():
    global swan_q, swan_temp
    while swan_q:
        x, y = swan_q.popleft()
        if x == sx and y == sy:
            return True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and swan_visited[nx][ny] == 0:
                if graph[nx][ny] != 'X':
                    swan_q.append((nx, ny))
                else:
                    swan_temp.append((nx, ny))
                swan_visited[nx][ny] = 1

    swan_q = swan_temp
    swan_temp = deque()
    return False

def melting():
    global water_q, water_temp
    while water_q:
        x, y = water_q.popleft()
        graph[x][y] = '.'
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and water_visited[nx][ny] == 0:
                if graph[nx][ny] == '.':
                    water_q.append((nx, ny))
                else:
                    water_temp.append((nx, ny))
                water_visited[nx][ny] = 1

    water_q = water_temp
    water_temp = deque()

day = 0
while True:
    # 빙판 녹음
    melting()

    # 백조가 만나는지 확인
    if check():
        break

    day += 1

print(day)