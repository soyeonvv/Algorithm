def destroy(d, s):
    for i in range(s):
        nx, ny = sx + dx[d] * (i + 1), sy + dy[d] * (i + 1)
        graph[nx][ny] = 0

def make_list(x, y):
    d = -1
    while True:
        if x < 0 or x >= n or y < 0 or y >= n:
            break
        visited[x][y] = True
        lst.append(graph[x][y])
        nd = (d + 1) % 4
        nx, ny = x + direction[nd][0], y + direction[nd][1]

        if visited[nx][ny]:
            nd = d
            nx, ny = x + direction[nd][0], y + direction[nd][1]

        x, y, d = nx, ny, nd

def blast():
    global lst, result
    flag = 0
    # 0 삭제
    lst = [i for i in lst if i != 0]
    # 4개 이상 연속 구슬 폭발
    cnt, x = 0, 0
    for i in range(len(lst)):
        if lst[i] == x:
            cnt += 1
        else:
            if cnt >= 4:
                flag = 1
                result[x] += cnt
                for j in range(i - cnt, i):
                    lst[j] = 0
            x = lst[i]
            cnt = 1
    if cnt >= 4:
        flag = 1
        result[x] += cnt
        for j in range(1, cnt + 1):
            lst[len(lst) - j] = 0

    return flag

def expand():
    if not lst:
        return []
    cnt, x = 0, lst[0]
    new_lst = []
    for i in range(len(lst)):
        if lst[i] == x:
            cnt += 1
        else:
            new_lst.append(cnt)
            new_lst.append(x)
            x = lst[i]
            cnt = 1
    new_lst.append(cnt)
    new_lst.append(x)
    return new_lst

def place(lst, x, y):
    new_graph = [[0] * n for _ in range(n)]

    if not lst:
        return new_graph

    d, i = -1, 0
    while True:
        if x < 0 or x >= n or y < 0 or y >= n:
            break
        if i >= len(lst):
            break
        visited[x][y] = True
        new_graph[x][y] = lst[i]
        nd = (d + 1) % 4
        nx, ny = x + direction[nd][0], y + direction[nd][1]

        if visited[nx][ny]:
            nd = d
            nx, ny = x + direction[nd][0], y + direction[nd][1]

        x, y, d, i = nx, ny, nd, i + 1

    return new_graph

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
command = [list(map(int, input().split())) for _ in range(m)]
visited = [[False] * n for _ in range(n)]
# 상어 위치
sx, sy = (n - 1) // 2, (n - 1) // 2

lst = []
result = [0, 0, 0, 0]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 회전 탐색 (좌 하 우 상)
direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]

for d, s in command:
    destroy(d - 1, s)
    make_list(sx, sy)
    visited = [[False] * n for _ in range(n)]
    flag = 1
    while flag:
        flag = blast()
    expand_lst = [0] + expand()
    graph = place(expand_lst, sx, sy)
    visited = [[False] * n for _ in range(n)]
    lst.clear()

answer = result[1] + result[2] * 2 + result[3] * 3
print(answer)