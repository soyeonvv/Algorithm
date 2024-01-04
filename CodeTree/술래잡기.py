n, m, h, k = map(int, input().split())
graph = [[[] for _ in range(n)] for _ in range(n)]
tree = [[0] * n for _ in range(n)]

# 술래
chaser = [n // 2, n // 2, -1, 0]
visited = [[0] * n for _ in range(n)]
# 도망자
fugitives = []
check = [0] * m
for i in range(m):
    x, y, d = map(int, input().split())
    graph[x - 1][y - 1].append(i)
    fugitives.append([x - 1, y - 1, d])
# 나무
for _ in range(h):
    x, y = map(int, input().split())
    tree[x - 1][y - 1] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def move_fugitives():
    num = 0
    for x, y, d in fugitives:
        if check[num] == 0 and abs(chaser[0] - x) + abs(chaser[1] - y) <= 3:
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                d = (d + 2) % 4
                fugitives[num][2] = d
                nx, ny = x + dx[d], y + dy[d]
            if not (nx == chaser[0] and ny == chaser[1]):
                fugitives[num][0], fugitives[num][1] = nx, ny
                graph[nx][ny].append(num)
                graph[x][y].remove(num)
        num += 1

def move_chaser(t):
    x, y, d, v = chaser
    if x == 0 and y == 0:
        d = 2
    if t != 1 and x == n // 2 and y == n // 2:
        d = -1
    if v == 0:
        visited[x][y] = 1
        nd = (d + 1) % 4
        nx, ny = x + dx[nd], y + dy[nd]
        if visited[nx][ny] == 1:
            nd = d
            nx, ny = x + dx[nd], y + dy[nd]
    if v == 1:
        visited[x][y] = 0
        nx, ny, nd = x + dx[d], y + dy[d], d
        if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] == 0:
            nd = (d - 1) % 4
            nx, ny = x + dx[nd], y + dy[nd]
    chaser[0], chaser[1], chaser[2] = nx, ny, nd
    if (nx == 0 and ny == 0) or (nx == n // 2 and ny == n // 2):
        chaser[3] = (v + 1) % 2

def get_fugitives():
    x, y, d, v = chaser
    cnt = 0
    # 시야 방향 설정
    if v == 0:
        nd = (d + 1) % 4
        nx, ny = x + dx[nd], y + dy[nd]
        if visited[nx][ny] == 1:
            nd = d
    if v == 1:
        nx, ny, nd = x + dx[d], y + dy[d], d
        if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] == 0:
            nd = (d - 1) % 4
    # 도망자 잡기
    for i in range(3):
        nx, ny = x + dx[nd] * i, y + dy[nd] * i
        if 0 <= nx < n and 0 <= ny < n and tree[nx][ny] == 0 and graph[nx][ny]:
            cnt += len(graph[nx][ny])
            for num in graph[nx][ny]:
                check[num] = 1
            graph[nx][ny].clear()
    return cnt

score = 0
for i in range(1, k + 1):
    # 도망자 이동
    move_fugitives()
    # 술래 이동
    move_chaser(i)
    # 도망자 잡기
    score += i * get_fugitives()

print(score)