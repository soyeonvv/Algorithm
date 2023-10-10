from collections import deque

def init():
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'R':
                rx, ry = i, j
            elif graph[i][j] == 'B':
                bx, by = i, j
    queue.append((rx, ry, bx, by, 0))
    visited[rx][ry][bx][by] = 1

def bfs():
    while queue:
        crx, cry, cbx, cby, cnt = queue.popleft()
        if cnt > 10:
            break
        if graph[crx][cry] == 'O' and graph[cbx][cby] != 'O':
            print(cnt)
            return
        for i in range(4):
            nrx, nry, nbx, nby = crx, cry, cbx, cby
            while True:
                if graph[nrx][nry] != '#' and graph[nrx][nry] != 'O':
                    nrx += dx[i]
                    nry += dy[i]
                else:
                    if graph[nrx][nry] == '#':
                        nrx -= dx[i]
                        nry -= dy[i]
                    break

            while True:
                if graph[nbx][nby] != '#' and graph[nbx][nby] != 'O':
                    nbx += dx[i]
                    nby += dy[i]
                else:
                    if graph[nbx][nby] == '#':
                        nbx -= dx[i]
                        nby -= dy[i]
                    break

            if nrx == nbx and nry == nby:
                if graph[nrx][nry] != 'O':
                    r_dist = abs(nrx - crx) + abs(nry - cry)
                    b_dist = abs(nbx - cbx) + abs(nby - cby)
                    if r_dist > b_dist:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

            if visited[nrx][nry][nbx][nby] == 0:
                visited[nrx][nry][nbx][nby] = 1
                queue.append((nrx, nry, nbx, nby, cnt + 1))

    print(-1)

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visited = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

init()
bfs()