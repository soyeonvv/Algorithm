def check():
    for i in range(n):
        now = i
        for j in range(h):
            if graph[j][now] == 1:
                now += 1
            elif now > 0 and graph[j][now - 1] == 1:
                now -= 1
        if now != i:
            return False
    return True

def dfs(cnt, x, y):
    global answer
    if check():
        answer = min(answer, cnt)
        return
    elif cnt == 3 or answer <= cnt:
        return

    for i in range(x, h):
        if i == x:
            now = y
        else:
            now = 0
        for j in range(now, n - 1):
            if graph[i][j] == 0 and graph[i][j + 1] == 0:
                if j > 0 and graph[i][j - 1] == 1:
                    continue
                graph[i][j] = 1
                dfs(cnt + 1, i, j + 2)
                graph[i][j] = 0

n, m, h = map(int, input().split())
graph = [[0] * n for _ in range(h)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1

answer = 4
dfs(0, 0, 0)
print(answer if answer <= 3 else -1)