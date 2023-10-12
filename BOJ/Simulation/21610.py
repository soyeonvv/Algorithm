from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
command = [list(map(int, input().split())) for _ in range(m)]

# 초기 구름
cloud = [[0] * n for _ in range(n)]
cloud[n - 1][0], cloud[n - 1][1], cloud[n - 2][0], cloud[n - 2][1] = 1, 1, 1, 1
cloud_p = deque()
c = []

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def move(d, s):
    for i in range(n):
        for j in range(n):
            if cloud[i][j] == 1:
                cloud[i][j] = 0
                nx, ny = (i + dx[d] * s) % n, (j + dy[d] * s) % n
                graph[nx][ny] += 1
                cloud_p.append((nx, ny))

def copybug():
    while cloud_p:
        x, y = cloud_p.popleft()
        c.append((x, y))
        cnt = 0
        for dx, dy in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 0:
                cnt += 1
        graph[x][y] += cnt

def create():
    for i in range(n):
        for j in range(n):
            if (i, j) not in c and graph[i][j] >= 2:
                graph[i][j] -= 2
                cloud[i][j] = 1

for d, s in command:
    # 구름 이동
    move(d - 1, s)
    # 물복사버그
    copybug()
    # 구름 생성
    create()
    # c 초기화
    c.clear()

answer = 0
for i in graph:
    answer += sum(i)
print(answer)