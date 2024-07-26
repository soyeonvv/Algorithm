from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, idx, visited):
    queue = deque()
    cnt = 1
    group[x][y] = idx
    visited[x][y] = 1
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and graph[nx][ny] == graph[x][y]:
                cnt += 1
                group[nx][ny] = idx
                visited[nx][ny] = 1
                queue.append((nx, ny))

    return cnt

def divide_group():
    visited = [[0] * n for _ in range(n)]
    cnt = {}

    idx = 1
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                cnt[idx] = bfs(i, j, idx, visited)
                idx += 1

    return cnt

def get_score():
    value = 0

    for x in range(n):
        for y in range(n):
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < n and 0 <= ny < n and group[nx][ny] != group[x][y]:
                    a_cnt, b_cnt = group_cnt[group[x][y]], group_cnt[group[nx][ny]]
                    a_num, b_num = graph[x][y], graph[nx][ny]
                    value += (a_cnt + b_cnt) * a_num * b_num

    return value // 2

def rotate_cross():
    # 전체 그래프 반시계 90 회전
    copy_graph = [x[::-1] for x in list(map(list, zip(*graph[::-1])))[::-1]]
    # 십자 모양만 바꾸기
    for x in range(n):
        graph[x][n // 2] = copy_graph[x][n // 2]
    for y in range(n):
        graph[n // 2][y] = copy_graph[n // 2][y]

def rotate_square(len):
    copy_graph = [row[:] for row in graph]
    for i in range(4):
        cx = 0 if i < 2 else n // 2 + 1
        cy = 0 if i % 2 == 0 else n // 2 + 1
        for x in range(cx, cx + len):
            for y in range(cy, cy + len):
                ox, oy = x - cx, y - cy
                rx, ry = oy, len - ox - 1
                copy_graph[cx + rx][cy + ry] = graph[x][y]
        for x in range(cx, cx + len):
            for y in range(cy, cy + len):
                graph[x][y] = copy_graph[x][y]

answer = 0
for t in range(4):
    # 그룹 나누기
    group = [row[:] for row in graph]
    group_cnt = divide_group()

    # 예술 점수 구하기
    answer += get_score()

    if t == 3:
        break

    # 십자 모양 회전
    rotate_cross()
    # 4개 정사각형 회전
    rotate_square(n // 2)

print(answer)