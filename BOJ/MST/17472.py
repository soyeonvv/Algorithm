from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
island = []
bridges = set()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, z):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    graph[x][y] = z

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 0 and visited[nx][ny] == 0:
                    graph[nx][ny] = z
                    island.append((nx, ny, z))
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

def make_bridge(x, y, z):
    queue = deque()
    for i in range(4):
        queue.append((x, y, 0, i))

    while queue:
        x, y, dist, d = queue.popleft()
        if graph[x][y] != 0 and graph[x][y] != z:
            if dist > 2:
                bridges.add((dist - 1, z, graph[x][y]))
            continue
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != z:
            queue.append((nx, ny, dist + 1, d))

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a, b = find_parent(a), find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 섬 구분하기
num = 1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            island.append((i, j, num))
            bfs(i, j, num)
            num += 1

# 다리 놓기
for x, y, z in island:
    make_bridge(x, y, z)

bridges = list(bridges)
bridges.sort()
parent = [i for i in range(num)]

answer, cnt = 0, 0
for distance, start, end in bridges:
    if find_parent(start) != find_parent(end):
        cnt += 1
        union(start, end)
        answer += distance

if answer == 0 or cnt != num - 2:
    print(-1)
else:
    print(answer)