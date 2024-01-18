from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = 0, 0
visited = []

def bfs(x, y, graph):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    area = [(x, y)]
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    area.append((nx, ny))
                    cnt += 1
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

    return area, cnt

def solution(land):
    answer = 0
    global n, m, visited
    n, m = len(land), len(land[0])
    visited = [[0] * m for _ in range(n)]

    num = 0
    oil = [0]
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == 0:
                area, cnt = bfs(i, j, land)
                num += 1
                for x, y in area:
                    land[x][y] = num
                oil.append(cnt)

    for j in range(m):
        col = []
        result = 0
        for i in range(n):
            if land[i][j] != 0 and land[i][j] not in col:
                col.append(land[i][j])
        for i in col:
            result += oil[i]
        answer = max(answer, result)

    return answer