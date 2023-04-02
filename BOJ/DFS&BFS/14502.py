'''
# BFS - Python3 시간 초과
from collections import deque
import copy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

zero_cnt = 0 # 초기 상태의 0의 개수

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zero_cnt += 1

max_result = 0

queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    test_graph = copy.deepcopy(graph)
    visited = [[0] * m for _ in range(n)]
    global max_result
    result = 0

    for i in range(n):
        for j in range(m):
            if test_graph[i][j] == 2:
                visited[i][j] = 1
                queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if test_graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    result += 1
                    queue.append((nx, ny))

    max_result = max(max_result, zero_cnt - result)

def create_wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                create_wall(cnt + 1)
                graph[i][j] = 0

create_wall(0)
print(max_result - 3)
'''

# combinations 사용
from collections import deque
from itertools import combinations
import copy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b, graph):
    virus = 0
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                virus += 1
                queue.append((nx, ny))

    return virus

zero_cnt = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zero_cnt.append([i, j])

wall_list = list(combinations(zero_cnt, 3))

result = len(zero_cnt)

for wall_position in wall_list:
    test_graph = copy.deepcopy(graph)

    for wall in wall_position:
        wall_x, wall_y = wall
        test_graph[wall_x][wall_y] = 1
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                cnt += bfs(i, j, test_graph)
    
    if cnt < result:
        result = cnt

print(len(zero_cnt) - result - 3)