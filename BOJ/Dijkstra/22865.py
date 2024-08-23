import heapq

INF = int(1e9)

n = int(input())
graph = [[] for _ in range(n + 1)]
a, b, c = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    graph[y].append((x, z))

def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now  = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i, j in graph[now]:
            cost = dist + j
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

    return distance

a_dist = dijkstra(a)
b_dist = dijkstra(b)
c_dist = dijkstra(c)

answer, result = 0, 0
for i in range(1, n + 1):
    v = min(a_dist[i], b_dist[i], c_dist[i])
    if result < v:
        result = v
        answer = i
        
print(answer)