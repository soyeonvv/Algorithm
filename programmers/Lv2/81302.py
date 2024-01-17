from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(graph):
    p = []
    for i in range(5):
        for j in range(5):
            if graph[i][j] == 'P':
                p.append((i, j))
    
    for x, y in p:
        queue = deque()
        visited = [[-1] * 5 for _ in range(5)]
        queue.append((x, y))
        visited[x][y] = 0
        
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == -1:
                    if graph[nx][ny] == 'O':
                        queue.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1
                    if graph[nx][ny] == 'P' and visited[x][y] <= 1:
                        return 0
    return 1
                
def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))

    return answer