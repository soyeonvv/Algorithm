from collections import deque

graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    result = int(graph[x][y])
    graph[x][y] = 'X'

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if graph[nx][ny] != 'X':
                    result += int(graph[nx][ny])
                    graph[nx][ny] = 'X'
                    queue.append((nx, ny))

    return result

def solution(maps):
    answer = []

    for i in maps:
        graph.append(list(i))
    
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] != 'X':
                answer.append(bfs(i, j))

    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()

    return answer