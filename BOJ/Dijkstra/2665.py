import heapq

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(x, y):
    q = []
    heapq.heappush(q, (0, x, y))
    visited[x][y] = 1

    while q:
        cost, qx, qy = heapq.heappop(q)
        if qx == n - 1 and qy == n - 1:
            return cost
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    if graph[nx][ny] == 0:
                        heapq.heappush(q, (cost + 1, nx, ny))
                    else:
                        heapq.heappush(q, (cost, nx, ny))

print(dijkstra(0, 0))