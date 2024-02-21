n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
answer = 0

def boomerang(x, y, nx, ny, visited):
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        return False
    if visited[x][y] == 1 or visited[nx][y] == 1 or visited[x][ny] == 1:
        return False
    visited[x][y], visited[nx][y], visited[x][ny] = 1, 1, 1
    return True

def solve(x, y, total, visited):
    global answer
    if y == m:
        y = 0
        x += 1
    if x == n:
        answer = max(answer, total)
        return

    if boomerang(x, y, x + 1, y - 1, visited):
        solve(x, y + 1, total + graph[x][y] * 2 + graph[x + 1][y] + graph[x][y - 1], visited)
        visited[x][y], visited[x + 1][y], visited[x][y - 1] = 0, 0, 0
    if boomerang(x, y, x - 1, y - 1, visited):
        solve(x, y + 1, total + graph[x][y] * 2 + graph[x - 1][y] + graph[x][y - 1], visited)
        visited[x][y], visited[x - 1][y], visited[x][y - 1] = 0, 0, 0
    if boomerang(x, y, x - 1, y + 1, visited):
        solve(x, y + 1, total + graph[x][y] * 2 + graph[x - 1][y] + graph[x][y + 1], visited)
        visited[x][y], visited[x - 1][y], visited[x][y + 1] = 0, 0, 0
    if boomerang(x, y, x + 1, y + 1, visited):
        solve(x, y + 1, total + graph[x][y] * 2 + graph[x + 1][y] + graph[x][y + 1], visited)
        visited[x][y], visited[x + 1][y], visited[x][y + 1] = 0, 0, 0
    solve(x, y + 1, total, visited)

solve(0, 0, 0, visited)
print(answer)