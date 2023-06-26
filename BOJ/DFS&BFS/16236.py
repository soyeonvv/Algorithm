import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

answer = 0
fish, cnt = 0, 0
shark_size = 2
shark_x, shark_y = 0, 0

for i in range(n):
    for j in range(n):
        if 0 < graph[i][j] <= 6:
            cnt += 1
        elif graph[i][j] == 9:
            shark_x, shark_y = i, j
            graph[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(shark_x, shark_y):
    queue = deque()
    queue.append((shark_x, shark_y, 0))
    visited = [[0] * n for _ in range(n)]
    visited[shark_x][shark_y] = 1
    min_dist = INF
    distance = []

    while queue:
        x, y, dist = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if shark_size >= graph[nx][ny]:
                    visited[nx][ny] = 1
                    if 0 < graph[nx][ny] < shark_size:
                        min_dist = dist
                        distance.append((dist + 1, nx, ny))
                    if dist + 1 <= min_dist:
                        queue.append((nx, ny, dist + 1))
    
    if distance:
        distance.sort()
        return distance[0]
    else:
        return False

while cnt:
    result = bfs(shark_x, shark_y)

    if not result:
        break

    shark_x, shark_y = result[1], result[2]
    answer += result[0]
    fish += 1
    cnt -= 1
    
    if shark_size == fish:
        shark_size += 1
        fish = 0

    graph[shark_x][shark_y] = 0

print(answer)