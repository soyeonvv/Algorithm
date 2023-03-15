from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        a, b, c = queue.popleft()
        if a == n - 1 and b == m - 1:
            return visited[a][b][c]
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1 and c == 0:
                visited[nx][ny][1] = visited[a][b][c] + 1
                queue.append((nx, ny, 1))
            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                queue.append((nx, ny, c))

    return -1

print(bfs(0, 0, 0))