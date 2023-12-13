from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
block = [[0] * n for _ in range(n)]
people = [[-1, -1] for _ in range(m)]
store = []
check = [0] * m
for _ in range(m):
    x, y = map(int, input().split())
    store.append([x - 1, y - 1])

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def get_distance(x, y, ex, ey):
    queue = deque()
    visited = [[-1] * n for _ in range(n)]
    queue.append((x, y))
    visited[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if block[nx][ny] == 0 and visited[nx][ny] == -1:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    if nx == ex and ny == ey:
                        return visited[nx][ny]

    return -1

def step1():
    p = 0
    for px, py in people:
        if px != -1 and py != -1 and check[p] == 0:
            distance = [-1] * 4
            for i in range(4):
                nx, ny = px + dx[i], py + dy[i]
                if 0 <= nx < n and 0 <= ny < n and block[nx][ny] == 0:
                    if nx == store[p][0] and ny == store[p][1]:
                        distance[i] = 0
                        break
                    distance[i] = get_distance(nx, ny, store[p][0], store[p][1])
            distance_ = [i for i in distance if i != -1]
            d = distance.index(min(distance_))
            nx, ny = px + dx[d], py + dy[d]
            people[p] = [nx, ny]
        p += 1

def step2():
    p = 0
    b = []
    for px, py in people:
        if px != -1 and py != -1 and check[p] == 0:
            if px == store[p][0] and py == store[p][1]:
                check[p] = 1
                b.append((px, py))
        p += 1
    for x, y in b:
        block[x][y] = 1

def step3():
    if t - 1 < m:
        if check[t - 1] == 0:
            sx, sy = store[t - 1]
            candidates = []
            queue = deque()
            visited = [[-1] * n for _ in range(n)]
            queue.append((sx, sy))
            visited[sx][sy] = 0

            while queue:
                x, y = queue.popleft()

                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n and block[nx][ny] == 0 and visited[nx][ny] == -1:
                        queue.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1
                        if graph[nx][ny] == 1:
                            candidates.append((visited[nx][ny], nx, ny))

            candidates.sort(key=lambda x:(x[0], x[1], x[2]))
            nx, ny = candidates[0][1], candidates[0][2]
            people[t - 1] = [nx, ny]
            block[nx][ny] = 1

t = 0
while True:
    t += 1
    # 1번
    step1()
    # 2번
    step2()
    # 3번
    step3()

    if check.count(1) == m:
        break

print(t)