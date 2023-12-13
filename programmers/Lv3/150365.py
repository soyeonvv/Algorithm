from collections import deque

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
d = ['d', 'l', 'r', 'u']

def manhattan(x, y, r, c):
    return abs(x - r) + abs(y - c)

def solution(n, m, x, y, r, c, k):
    answer = ''
    graph = [[0] * m for _ in range(n)]
    graph[x - 1][y - 1], graph[r - 1][c - 1] = 'S', 'E'

    # 경로 찾기
    if manhattan(x, y, r, c) > k or (manhattan(x, y, r, c) - k) % 2 != 0:
        return 'impossible'

    queue = deque()
    queue.append((x - 1, y - 1, 0, ''))

    while queue:
        x, y, cnt, route = queue.popleft()
        if graph[x][y] == 'E' and (k - cnt) % 2 != 0:
            return 'impossible'
        elif graph[x][y] == 'E' and cnt == k:
            return route

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if manhattan(nx + 1, ny + 1, r, c) + cnt + 1 > k:
                    continue
                queue.append((nx, ny, cnt + 1, route + d[i]))
                break

    return answer