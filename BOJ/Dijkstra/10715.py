import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
visited = [0] * (n + 1)
sum = 0

for _ in range(0, m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    graph[y].append((x, z))
    sum += z

result = sum

q = []
heapq.heappush(q, (0, 1))
distance[1] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    visited[now] = 1
    
    for i in graph[now]:
        if visited[i[0]] == 1:
            sum -= i[1]
    result = min(result, dist * c + sum)
    
    for i in graph[now]:
        if distance[i[0]] > dist + i[1]:
            distance[i[0]] = dist + i[1]
            heapq.heappush(q, (dist + i[1], i[0]))

print(result)