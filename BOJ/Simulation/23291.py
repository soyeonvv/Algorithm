n, k = map(int, input().split())
graph = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0

def rotate():
    global graph
    while True:
        l = len(graph)
        if l >= 2:
            for i in range(len(graph)):
                for j in range(len(graph[i])):
                    if graph[i][j] == 0:
                        x = j
                        break
            if len(graph[l - 1]) - x < l:
                return
            bottom = graph[l - 1][x:]
            rotate_graph = [[fish for fish in graph[i][:x]] for i in range(l)]
            rotate_graph = list(map(list, zip(*rotate_graph[::-1])))
            for i in range(len(rotate_graph)):
                while len(rotate_graph[i]) < len(bottom):
                    rotate_graph[i].append(0)
            graph = rotate_graph + [bottom]

def control():
    global graph
    new_graph = [[0] * len(graph[x]) for x in range(len(graph))]
    for x in range(len(graph)):
        for y in range(len(graph[x])):
            if graph[x][y] != 0:
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < len(graph) and 0 <= ny < len(graph[x]) and graph[nx][ny] != 0:
                        if graph[x][y] > graph[nx][ny]:
                            d = (graph[x][y] - graph[nx][ny]) // 5
                            if d > 0:
                                new_graph[x][y] -= d
                        else:
                            d = (graph[nx][ny] - graph[x][y]) // 5
                            if d > 0:
                                new_graph[x][y] += d
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            graph[i][j] += new_graph[i][j]

def line():
    line_graph = []
    rotate_graph = list(map(list, zip(*graph[::-1])))
    for line in rotate_graph:
        line_graph.extend([fish for fish in line if fish != 0])
    return line_graph

def rotate2():
    global graph
    # 첫번째 회전
    line1 = graph[:n//2][::-1]
    line2 = graph[n//2:]
    graph = [line1, line2]
    # 두번째 회전
    block1 = [graph[0][:n // 4], graph[1][:n // 4]]
    block1 = [lst[::-1] for lst in block1[::-1]]
    block2 = [graph[0][n // 4:], graph[1][n // 4:]]
    graph = block1 +block2

while True:
    # 물고기 수가 가장 적은 어항에 물고기 한 마리 넣기
    min_fish = min(graph)
    for i in range(n):
        if graph[i] == min_fish:
            graph[i] += 1

    # 가장 왼쪽에 있는 어항 올리기
    graph = [[graph[0]] + [0] * (n - 1), [x for x in graph[1:]]]

    # 2개 이상 쌓여있는 어항 공중 부양 후 시계방향 90도 회전
    rotate()

    # 물고기 수 조절
    control()

    # 일렬로
    graph = line()

    # n / 2 공중 부양 후 시계방향 90도 회전
    rotate2()

    # 물고기 수 조절
    control()

    # 일렬로
    graph = line()

    cnt += 1
    if max(graph) - min(graph) <= k:
        break

print(cnt)