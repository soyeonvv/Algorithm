import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    t_done = [0] * (n + 1)

    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    
    queue = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            t_done[i] = time[i]

    while queue:
        now = queue.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            t_done[i] = max(t_done[i], t_done[now] + time[i])
            if indegree[i] == 0:
                queue.append(i)

    w = int(input())
    print(t_done[w])