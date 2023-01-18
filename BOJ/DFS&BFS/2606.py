# BFS
from collections import deque
    
n = int(input())
v = int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for i in range(v):
    a, b = (map(int, input().split()))
    graph[a] += [b]
    graph[b] += [a]
queue = deque([1])
while queue:
    c = queue.popleft()
    for nx in graph[c]:
        if visited[nx] == 0:
            queue.append(nx)
            visited[nx] = 1
print(sum(visited)-1)

# DFS
'''
n = int(input())
v = int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for i in range(v):
    a, b = (map(int, input().split()))
    graph[a] += [b]
    graph[b] += [a]
def dfs(v):
    visited[v] = 1
    for nx in graph[v]:
        if visited[nx] == 0:
            dfs(nx)
dfs(1)
print(sum(visited)-1)
'''