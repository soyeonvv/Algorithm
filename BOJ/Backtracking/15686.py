import sys
sys.setrecursionlimit(10**6)
INF = int(1e9)

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []

for col in range(n):
    for row in range(n):
        if graph[col][row] == 1:
            house.append((col, row))
        if graph[col][row] == 2:
            chicken.append((col, row))

visited = [0] * len(chicken)
result = INF

def dfs(x, cnt):
    global result
    if cnt == m:
        answer = 0
        
        for i in house:
            distance = INF
            for j in range(len(visited)):
                if visited[j] == 1:
                    dist = abs(i[0] - chicken[j][0]) + abs(i[1] - chicken[j][1])
                    distance = min(distance, dist)
            
            answer += distance

        result = min(result, answer)
        return

    for i in range(x, len(chicken)):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i + 1, cnt + 1)
            visited[i] = 0

dfs(0, 0)
print(result)