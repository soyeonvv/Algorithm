from collections import deque
INF = int(1e9)

n = int(input())
population = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    lst = list(map(int, input().split()))
    for j in lst[1:]:
        graph[i].append(j)

def bfs(area):
    queue = deque()
    visited = [0] * (n + 1)
    queue.append(area[0])
    visited[area[0]] = 1

    p, cnt = 0, 1
    while queue:
        now = queue.popleft()
        p += population[now]
        for i in graph[now]:
            if i in area and visited[i] == 0:
                cnt += 1
                queue.append(i)
                visited[i] = 1

    if cnt == len(area):
        return p
    else:
        return -1

def dfs(cnt, start, num):
    global answer
    if cnt == num:
        area1, area2 = [], []
        for i in range(1, n + 1):
            if visited[i]:
                area1.append(i)
            else:
                area2.append(i)
        p1, p2 = bfs(area1), bfs(area2)
        if p1 == -1 or p2 == -1:
            return
        answer = min(answer, abs(p1 - p2))
        return

    for i in range(start, n + 1):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(cnt + 1, i + 1, num)
        visited[i] = 0

answer = INF
for i in range(1, n // 2 + 1):
    visited = [0] * (n + 1)
    dfs(0, 1, i)

if answer == INF:
    print(-1)
else:
    print(answer)