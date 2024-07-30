n, m, k, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ddx = [-1, 1, 1, -1]
ddy = [1, 1, -1, -1]

def grow_and_breed():
    new_graph = [row[:] for row in graph]
    for x in range(n):
        for y in range(n):
            if graph[x][y] > 0:
                grow_cnt, breed_cnt = 0, 0
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] > 0:
                            grow_cnt += 1
                        elif graph[nx][ny] == 0:
                            breed_cnt += 1
                # 나무 성장
                graph[x][y] += grow_cnt
                # 나무 번식
                if breed_cnt == 0:
                    continue
                breed = graph[x][y] // breed_cnt
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                        new_graph[nx][ny] += breed

    for x in range(n):
        for y in range(n):
            if graph[x][y] == 0 and new_graph[x][y] > 0:
                graph[x][y] = new_graph[x][y]

def pesticide_pos():
    candidates = []
    for x in range(n):
        for y in range(n):
            if graph[x][y] > 0:
                cnt = graph[x][y]
                for d in range(4):
                    for i in range(1, k + 1):
                        nx, ny = x + ddx[d] * i, y + ddy[d] * i
                        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > 0:
                            cnt += graph[nx][ny]
                        else:
                            break
                candidates.append((cnt, x, y))

    candidates.sort(key=lambda x:(-x[0], x[1], x[2]))
    if candidates:
        return candidates[0]
    else:
        return -1

def exterminate(x, y):
    pesticide.append([c, x, y])
    graph[x][y] = -2
    for d in range(4):
        for i in range(1, k + 1):
            flag = 0
            nx, ny = x + ddx[d] * i, y + ddy[d] * i
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] >= 0 or graph[nx][ny] == -2:
                    if graph[nx][ny] == 0:
                        flag = 1
                    # 살충제 뿌린 곳 갱신
                    if graph[nx][ny] == -2:
                        flag = 1
                        for i, (p, q, r) in enumerate(pesticide):
                            if q == nx and r == ny:
                                pesticide[i][0] = c
                                break
                    else:
                        pesticide.append([c, nx, ny])
                        graph[nx][ny] = -2
                    if flag:
                        break
                else:
                    break

answer = 0
pesticide = []
for _ in range(m):
    # 나무 성장 & 번식
    grow_and_breed()

    # 제초제 유지
    for i in range(len(pesticide) - 1, -1, -1):
        pesticide[i][0] -= 1
        if pesticide[i][0] == 0:
            graph[pesticide[i][1]][pesticide[i][2]] = 0
            del pesticide[i]

    # 제초제 뿌릴 칸 찾기
    result = pesticide_pos()
    if result != -1:
        cnt, x, y = result
        answer += cnt

        # 제초제 뿌리기
        exterminate(x, y)

print(answer)