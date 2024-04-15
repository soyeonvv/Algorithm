from collections import deque

graph = [list(input()) for _ in range(8)]
visited = [[0] * 8 for _ in range(8)]
wx, wy = 7, 0

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

def move_wall():
    return [['.'] * 8] + graph[:-1]

queue = deque()
queue.append((wx, wy))
time = 0

while queue:
    visited = [[0] * 8 for _ in range(8)]

    for _ in range(len(queue)):
        x, y = queue.popleft()

        if graph[x][y] == '#':
            continue

        if x == 0:
            print(1)
            exit()

        # 욱제 이동
        for i in range(9):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= 8 or ny < 0 or ny >= 8 or graph[nx][ny] == '#' or visited[nx][ny]:
                continue

            visited[nx][ny] = 1
            queue.append((nx, ny))

    # 벽 이동
    graph = move_wall()

    time += 1
    if time == 9:
        print(1)
        exit()

print(0)