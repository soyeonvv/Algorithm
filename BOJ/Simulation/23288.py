from collections import deque

n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dice = [2, 1, 5, 6, 4, 3]
x, y, dd, answer = 0, 0, 1, 0

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def move_dice(direction):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if direction == 0: # 북
        dice[0], dice[1], dice[2], dice[3] = b, c, d, a
    if direction == 1: # 동
        dice[1], dice[3], dice[4], dice[5] = e, f, d, b
    elif direction == 2: # 남
        dice[0], dice[1], dice[2], dice[3] = d, a, b, c
    elif direction == 3: # 서
        dice[1], dice[3], dice[4], dice[5] = f, e, b, d

def bfs(x, y, num):
    queue = deque()
    visited = [[0] * m for _ in range(n)]
    queue.append((x, y))
    visited[x][y] = 1

    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] != 1:
                if graph[nx][ny] == num:
                    cnt += 1
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

    return cnt

for _ in range(k):
    # 굴러갈 수 없으면 방향 전환
    if not (0 <= x + dx[dd] < n and 0 <= y + dy[dd] < m):
        dd = (dd + 2) % 4

    x, y = x + dx[dd], y + dy[dd]

    # 주사위 굴리기
    move_dice(dd)

    # 점수 계산
    B = graph[x][y]
    answer += B * bfs(x, y, B)

    # 조건에 맞게 이동 방향 회전
    if dice[3] > graph[x][y]:
        dd = (dd + 1) % 4
    elif dice[3] < graph[x][y]:
        dd = (dd - 1) % 4

print(answer)