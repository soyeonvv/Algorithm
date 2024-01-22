import heapq
INF = int(1e9)

distance = []

def dijkstra(start, n, graph):
    global distance
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n + 1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    dijkstra(destination, n, graph)

    for i in sources:
        if distance[i] == INF:
            answer.append(-1)
        else:
            answer.append(distance[i])

    return answer