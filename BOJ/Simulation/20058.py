from collections import deque

n, q = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(2 ** n)]
l = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def turn(graph, x):
    new_graph = [[0] * (2 ** n) for _ in range(2 ** n)]

    for i in range(0, 2 ** n, 2 ** x):
        for j in range(0, 2 ** n, 2 ** x):
            for k in range(2 ** x):
                for m in range(2 ** x):
                    new_graph[i + k][j + m] = graph[i + (2 ** x - 1 - m)][j + k]

    return new_graph

def melt(graph):
    new_graph = [[0] * (2 ** n) for _ in range(2 ** n)]

    for i in range(2 ** n):
        for j in range(2 ** n):
            ice = 0
            for d in range(4):
                nx, ny = i + dx[d], j + dy[d]

                if 0 <= nx < 2 ** n and 0 <= ny < 2 ** n:
                    if graph[nx][ny] > 0:
                        ice += 1

            if ice < 3:
                new_graph[i][j] = graph[i][j] - 1
            else:
                new_graph[i][j] = graph[i][j]

    return new_graph

def bfs(x, y):
    global sum_ice
    queue = deque()
    queue.append((x, y))
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < 2 ** n and 0 <= ny < 2 ** n:
                if graph[nx][ny] > 0 and visited[nx][ny] == 0:
                    sum_ice += graph[nx][ny]
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += 1

    return cnt

for i in range(q):
    graph = turn(graph, l[i])
    graph = melt(graph)

visited = [[0] * (2 ** n) for _ in range(2 ** n)]
sum_ice, max_size = 0, 0

for i in range(2 ** n):
    for j in range(2 ** n):
        if graph[i][j] > 0 and visited[i][j] == 0:
            visited[i][j] = 1
            sum_ice += graph[i][j]
            max_size = max(max_size, bfs(i, j))

print(sum_ice)
print(max_size)