def fish_move():
    res = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            while temp[x][y]:
                d = temp[x][y].pop()
                for i in range(8):
                    nd = (d - i) % 8
                    nx, ny = x + dx[nd], y + dy[nd]
                    if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) != (sx, sy) and not smell[nx][ny]:
                        res[nx][ny].append(nd)
                        break
                else:
                    res[x][y].append(d)
    return res

def dfs(x, y, depth, cnt, visited):
    global sx, sy, fish_cnt, fish_smell
    if depth == 3:
        if fish_cnt < cnt:
            fish_cnt = cnt
            sx, sy = x, y
            fish_smell = visited[:]
        return
    for d in range(4):
        nx, ny = x + direction[d][0], y + direction[d][1]
        if 0 <= nx < 4 and 0 <= ny < 4:
            if (nx, ny) not in visited:
                visited.append((nx, ny))
                dfs(nx, ny, depth + 1, cnt + len(temp[nx][ny]), visited)
                visited.pop()
            else:
                dfs(nx, ny, depth + 1, cnt, visited)

m, s = map(int, input().split())
graph = [[[] for _ in range(4)] for _ in range(4)]

for _ in range(m):
    x, y, d = map(int, input().split())
    graph[x - 1][y - 1].append(d - 1)

sx, sy = map(int, input().split())
sx -= 1
sy -= 1
smell = [[0] * 4 for _ in range(4)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
direction = [(-1, 0), (0, -1), (1, 0), (0, 1)] # 상어 이동 (상 좌 하 우)

for _ in range(s):
    # 물고기 복제
    temp = [[k[:] for k in row] for row in graph]
    # 물고기 이동
    temp = fish_move()
    # 상어 이동
    fish_cnt = -1
    fish_smell = []
    dfs(sx, sy, 0, 0, [])
    for x, y in fish_smell:
        if temp[x][y]:
            temp[x][y] = []
            smell[x][y] = 3
    # 냄새 사라짐
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1
    # 마법
    for i in range(4):
        for j in range(4):
            if temp[i][j]:
                graph[i][j] += temp[i][j]

answer = 0
for i in range(4):
    for j in range(4):
        if graph[i][j]:
            answer += len(graph[i][j])
print(answer)