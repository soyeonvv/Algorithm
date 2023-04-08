import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    distance[start][start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[start][now] < dist:
            continue
        for i, j in graph[now]:
            cost = dist + j
            if cost < distance[start][i]:
                distance[start][i] = cost
                heapq.heappush(q, (cost, i))
                visited[i][start] = now
                
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [[INF] * (n + 1) for _ in range(n + 1)]
visited = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for i in range(1, n + 1):
    dijkstra(i)

for x in range(1, n + 1):
    for y in range(1, n + 1):
        if x == y:
            print("-", end=" ")
        else:
            print(visited[x][y], end=" ")
    print()