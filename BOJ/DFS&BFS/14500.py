import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, total, l):
    global result
    if result >= total + max_pos * (4 - l):
        return
    if l == 4:
        result = max(result, total)
        return
    else:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny <m and visited[nx][ny] == 0:
                if l == 2:
                    visited[nx][ny] = 1
                    dfs(x, y, total + graph[nx][ny], l + 1)
                    visited[nx][ny] = 0
                visited[nx][ny] = 1
                dfs(nx, ny, total + graph[nx][ny], l + 1)
                visited[nx][ny] = 0

max_pos = max(map(max, graph))
result = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, graph[i][j], 1)
        visited[i][j] = 0

print(result)