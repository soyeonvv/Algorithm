from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(n, m, hole):
    graph = [[0] * n for _ in range(m)]
    for x, y in hole:
        graph[m - y][x - 1] = -1

    queue = deque()
    visited = [[[-1] * 2 for _ in range(n)] for _ in range(m)]

    queue.append((m - 1, 0, 0))
    visited[m - 1][0][0] = 0

    while queue:
        x, y, shoes = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny][shoes] == -1 and graph[nx][ny] == 0:
                queue.append((nx, ny, shoes))
                visited[nx][ny][shoes] = visited[x][y][shoes] + 1
            if shoes == 0:
                nx += dx[i]
                ny += dy[i]
                if 0 <= nx < m and 0 <= ny < n and visited[nx][ny][1] == -1 and graph[nx][ny] == 0:
                    queue.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][shoes] + 1

    if visited[0][n - 1][0] == visited[0][n - 1][1] == -1:
        print(-1)
    elif -1 not in visited[0][n - 1]:
        print(min(visited[0][n - 1]))
    else:
        print(max(visited[0][n - 1]))