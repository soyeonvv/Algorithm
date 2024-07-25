from collections import deque

k, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(5)]
pieces = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def rotate(sx, sy, rotate_graph, flag):
    new_graph = [row[:] for row in rotate_graph]

    for x in range(sx, sx + 3):
        for y in range(sy, sy + 3):
            ox, oy = x - sx, y - sy
            if flag == 1:
                # 90
                rx, ry = oy, 3 - ox - 1
            elif flag == 2:
                # 180
                rx, ry = 3 - ox - 1, 3 - oy - 1
            else:
                # 270
                rx, ry = 3 - oy - 1, ox
            new_graph[sx + rx][sy + ry] = graph[x][y]

    for x in range(sx, sx + 3):
        for y in range(sy, sy + 3):
            rotate_graph[x][y] = new_graph[x][y]

    return rotate_graph

def bfs(x, y, graph, visited, flag):
    cnt = 1
    candidates = [(x, y)]
    queue = deque()
    visited[x][y] = 1
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if graph[nx][ny] == graph[x][y] and visited[nx][ny] == 0:
                    cnt += 1
                    candidates.append((nx, ny))
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

    if flag == 1 and cnt >= 3:
        for x, y in candidates:
            graph[x][y] = 0

    return cnt

def excavate(graph):
    relic_cnt = 0
    visited = [[0] * 5 for _ in range(5)]

    for i in range(5):
        for j in range(5):
            if visited[i][j] == 0:
                cnt = bfs(i, j, graph, visited, 0)
                if cnt >= 3:
                    relic_cnt += cnt

    return relic_cnt

answer = []
for _ in range(k):
    flag = 0

    # 9개 각각 3개 각도로 회전
    result = []
    for i in range(3):
        for j in range(3):
            for v in range(1, 4):
                copy_graph = [row[:] for row in graph]
                result.append([excavate(rotate(i, j, copy_graph, v)), v, j, i])

    # 회전 블럭 선택
    result.sort(key=lambda x:(-x[0], x[1], x[2], x[3]))
    cnt, deg, y, x = result[0]

    # 유물 획득 X > 즉시 종료
    if cnt == 0:
        break

    # 회전
    rotate(x, y, graph, deg)

    total = 0
    while True:
        # 유물 획득
        total_cnt = 0
        visited = [[0] * 5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                if visited[i][j] == 0:
                    relic_cnt = bfs(i, j, graph, visited, 1)
                    if relic_cnt >= 3:
                        total_cnt += relic_cnt

        if total_cnt == 0:
            answer.append(total)
            break
        else:
            total += total_cnt

        # 채우기
        for j in range(5):
            for i in range(4, -1, -1):
                if graph[i][j] == 0:
                    graph[i][j] = pieces.pop(0)

print(' '.join(map(str, answer)))