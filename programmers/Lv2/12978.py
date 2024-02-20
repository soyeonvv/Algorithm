import heapq
INF = int(1e9)

def dijkstra(start, graph, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i, j in graph[now]:
            cost = dist + j
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))
                
    return distance

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N)]
    distance = [INF] * N
    
    for a, b, c in road:
        graph[a - 1].append((b - 1, c))
        graph[b - 1].append((a - 1, c))
    
    time = dijkstra(0, graph, distance)
    for i in time:
        if i <= K:
            answer += 1

    return answer