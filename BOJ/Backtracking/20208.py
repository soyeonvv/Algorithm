n, m, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
hx, hy = 0, 0
milk = []
milk_cnt = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            hx, hy = i, j
        elif graph[i][j] == 2:
            milk.append((i, j))
            milk_cnt += 1
check = [0] * milk_cnt

def get_dist(sx, sy, ex, ey):
    dist = abs(sx - ex) + abs(sy - ey)
    return dist

def dfs(cnt, stats, x, y):
    global answer

    for i in range(milk_cnt):
        if check[i] == 0:
            dist = get_dist(x, y, milk[i][0], milk[i][1])
            if dist <= stats:
                check[i] = 1
                dfs(cnt + 1, stats - dist + h, milk[i][0], milk[i][1])
                check[i] = 0

    go_home = get_dist(x, y, hx, hy)
    if go_home <= stats:
        answer = max(answer, cnt)

answer = 0
dfs(0, m, hx, hy)
print(answer)