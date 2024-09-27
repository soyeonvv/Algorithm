n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 모든 정점 최단 거리 구하기
for c in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])

answer = int(1e9)

def dfs(order, cost):
    global answer
    if len(order) == n:
        answer = min(answer, cost)
        return
    
    for i in range(n):
        if i not in order:
            order.append(i)
            dfs(order, cost + graph[order[-2]][i])
            order.pop()

dfs([k], 0)
print(answer)