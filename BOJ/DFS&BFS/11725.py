import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, p):
    for i in graph[x]:
        if i == p:
            continue
        parent[i] = x
        dfs(i, x)

dfs(1, -1)
for i in range(2, n + 1):
    print(parent[i])