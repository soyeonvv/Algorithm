from collections import deque
from itertools import combinations

graph = [list(input()) for _ in range(5)]
positions = [(i, j) for i in range(5) for j in range(5)]
combs = list(combinations(positions, 7))
answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def checkS(comb):
    s = 0
    for x, y in comb:
        if graph[x][y] == 'S':
            s += 1
    if s >= 4:
        return True
    else:
        return False

def checkAdjacent(comb):
    visited = [0] * 7
    queue = deque()
    queue.append(comb[0])
    visited[0] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (nx, ny) in comb:
                idx = comb.index((nx, ny))
                if visited[idx] == 0:
                    queue.append((nx, ny))
                    visited[idx] = 1

    if 0 in visited:
        return False
    else:
        return True

for comb in combs:
    if checkS(comb):
        if checkAdjacent(comb):
            answer += 1

print(answer)