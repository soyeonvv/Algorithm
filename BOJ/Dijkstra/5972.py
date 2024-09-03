import heapq
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    distance = [INF] * (n + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i, j in graph[now]:
            cost = dist + j
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

    return distance[n]

print(dijkstra(1))