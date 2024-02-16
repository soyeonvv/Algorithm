from collections import deque

n, h, d = map(int, input().split())
graph = [list(input()) for _ in range(n)]
start = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'S':
            start = [i, j]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
visited = [[0] * n for _ in range(n)]

def bfs(x, y, H, D, cnt):
    queue.append((x, y, H, D, cnt))
    visited[x][y] = H

    while queue:
        x, y, H, D, cnt = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            nh, nd = H, D

            if 0 <= nx < n and 0 <= ny < n:
                # 안전지대 도착 여부 확인
                if graph[nx][ny] == 'E':
                    return cnt + 1
                # 우산 여부 확인
                if graph[nx][ny] == 'U':
                    nd = d
                    graph[nx][ny] = '.'
                # 우산이 없다면 체력 감소
                if nd == -1 and graph[nx][ny] == '.':
                    nh -= 1
                    # 6. 체력이 0이 되면 죽는다
                    if nh == 0:
                        continue
                # 우산이 있다면 내구도 감소
                elif nd != -1:
                    nd -= 1
                    # 5. 우산의 내구도가 0이 되면 우산이 사라진다.
                    if nd == 0:
                        nd = -1

                if visited[nx][ny] < nh:
                    visited[nx][ny] = nh
                    queue.append((nx, ny, nh, nd, cnt + 1))

    return -1

print(bfs(start[0], start[1], h, -1, 0))