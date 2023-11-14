from collections import deque

n, m, f = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
taxi_x, taxi_y = map(int, input().split())
passengers = [list(map(int, input().split())) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y): # 최단 거리 구하기
    visited = [[-1] * n for _ in range(n)]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 1 and visited[nx][ny] == -1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return visited

while passengers:
    # 택시 > 승객
    visited = bfs(taxi_x - 1, taxi_y - 1)
    for i in passengers:
        x, y = i[0], i[1]
        i.append(visited[x - 1][y - 1])
    passengers.sort(key=lambda x:(-x[4], -x[0], -x[1]))

    sx, sy, ex, ey, distance = passengers.pop()
    for i in passengers:
        i.pop()

    # 승객 > 목적지
    visited = bfs(sx - 1, sy - 1)
    distance2 = visited[ex - 1][ey - 1]
    taxi_x, taxi_y = ex, ey

    if distance == -1 or distance2 == -1:
        print(-1)
        exit(0)
    f -= distance
    if f < 0:
        break
    f -= distance2
    if f < 0:
        break
    f += distance2 * 2

if f < 0:
    print(-1)
else:
    print(f)