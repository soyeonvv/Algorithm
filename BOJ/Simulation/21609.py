from collections import deque

def bfs(x, y, num):
    queue = deque()
    queue.append((x, y))
    global cnt, rainbow
    cnt, rainbow = 1, 0
    block_list, rainbow_list = [(x, y)], []

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if graph[nx][ny] == num:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    cnt += 1
                    block_list.append((nx, ny))
                elif graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    cnt += 1
                    rainbow += 1
                    rainbow_list.append((nx, ny))

    for i, j in rainbow_list:
        visited[i][j] = 0
    return block_list + rainbow_list

def remove_block(block):
    global answer
    answer += block[0] ** 2
    for x, y in block[4]:
        graph[x][y] = -2

def gravity():
    for i in range(n - 2, -1, -1):
        for j in range(n):
            if graph[i][j] != -1:
                pointer = i
                while pointer + 1 < n and graph[pointer + 1][j] == -2:
                    graph[pointer + 1][j] = graph[pointer][j]
                    graph[pointer][j] = -2
                    pointer += 1

def rotate():
    global graph
    graph = [x[::-1] for x in list(map(list, zip(*graph[::-1])))[::-1]]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt, rainbow, answer = 0, 0, 0

while True:
    # 가장 큰 블록 그룹 찾기
    block = []
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if 1 <= graph[i][j] <= m and visited[i][j] == 0:
                visited[i][j] = 1
                group = bfs(i, j, graph[i][j])
                if cnt >= 2:
                    block.append([cnt, rainbow, i, j, group])

    if len(block) == 0:
        break
    block.sort(key=lambda x:(-x[0], -x[1], -x[2], -x[3]))

    # 블록 그룹 제거
    remove_block(block[0])
    # 중력 작용
    gravity()
    # 반시계 회전
    rotate()
    # 중력 작용
    gravity()

print(answer)