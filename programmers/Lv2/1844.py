from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, n, m, graph):
    queue = deque()
    visited = [[-1] * m for _ in range(n)]
    queue.append((x, y))
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    
    return visited[n - 1][m - 1]

def solution(maps):
    n, m = len(maps), len(maps[0])
    answer = bfs(0, 0, n, m, maps)
    return answer