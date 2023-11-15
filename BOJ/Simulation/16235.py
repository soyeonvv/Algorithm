n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
graph = [[5] * n for _ in range(n)]
tree = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

dead = []
for _ in range(k):
    # 봄 + 여름
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                tree[i][j].sort()
                live = []
                dead = 0
                for age in tree[i][j]:
                    if age <= graph[i][j]:
                        graph[i][j] -= age
                        live.append(age + 1)
                    else:
                        dead += age // 2
                graph[i][j] += dead
                tree[i][j].clear()
                tree[i][j].extend(live)

    # 가을
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                for x in tree[i][j]:
                    if x % 5 == 0:
                        for d in range(8):
                            nx, ny = i + dx[d], j + dy[d]
                            if 0 <= nx < n and 0 <= ny < n:
                                tree[nx][ny].append(1)

    # 겨울
    for i in range(n):
        for j in range(n):
            graph[i][j] += a[i][j]

cnt = 0
for i in range(n):
    for j in range(n):
        if tree[i][j]:
            cnt += len(tree[i][j])
print(cnt)