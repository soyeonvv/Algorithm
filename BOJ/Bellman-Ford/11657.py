import sys
input = sys.stdin.readline
INF = int(1e9)

def bf(start):
    distance[start] = 0
    for i in range(n):
        for j in range(m):
            now = edges[j][0]
            next_node = edges[j][1]
            dist = edges[j][2]
            if distance[now] != INF and distance[next_node] > distance[now] + dist:
                distance[next_node] = distance[now] + dist
                if i == n - 1:
                    return True
    return False


n, m = map(int, input().split())
edges = []
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

negative_cycle = bf(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2, n + 1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])