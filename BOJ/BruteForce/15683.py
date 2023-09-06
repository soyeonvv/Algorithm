import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상, 하, 좌, 우

cctv_direction = [
    [],
    [[0], [1], [2], [3]], # 1번 CCTV
    [[0, 1], [2, 3]], # 2번 CCTV
    [[0, 2], [0, 3], [1, 2], [1, 3]], # 3번 CCTV
    [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], # 4번 CCTV
    [[0, 1, 2, 3]] # 5번 CCTV
]

answer = int(1e9)
cctv = []

for i in range(n):
    for j in range(m):
        if 1 <= graph[i][j] <= 5:
            cctv.append((i, j, graph[i][j]))

def dfs(graph, depth):
    global answer
    if depth == len(cctv):
        answer = min(answer, cnt(graph))
        return
    else:
        graph_copy = copy.deepcopy(graph)
        x, y, type = cctv[depth]
        for directions in cctv_direction[type]:
            watch(x, y, directions, graph_copy)
            dfs(graph_copy, depth + 1)
            graph_copy = copy.deepcopy(graph)

def watch(x, y, directions, graph):
    for d in directions:
        nx, ny = x, y
        while True:
            nx += direction[d][0]
            ny += direction[d][1]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 6:
                    break
                elif graph[nx][ny] == 0:
                    graph[nx][ny] = '#'
            else:
                break

def cnt(graph):
    c = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                c += 1
    return c

dfs(graph, 0)
print(answer)