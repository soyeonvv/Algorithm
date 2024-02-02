from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_distance(graph, n, m, a, b):
    queue = deque()
    visited = [[-1] * m for _ in range(n)]
    queue.append((a[0], a[1]))
    visited[a[0]][a[1]] = 0
    
    while queue:
        x, y = queue.popleft()
        if x == b[0] and y == b[1]:
            return visited[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 'X' and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

    return -1

def solution(maps):
    n, m = len(maps), len(maps[0])
    s, e, l = [], [], []
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                s = [i, j]
            elif maps[i][j] == 'E':
                e = [i, j]
            elif maps[i][j] == 'L':
                l = [i, j]
                
    # 시작 > 레버 최단거리
    s_l = get_distance(maps, n, m, s, l)
    if s_l == -1:
        return -1
    answer = s_l
    
    # 레버 > 출구 최단거리
    l_e = get_distance(maps, n, m, l, e)
    if l_e == -1:
        return -1
    answer += l_e
    
    return answer