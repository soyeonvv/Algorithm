n, m, k = map(int, input().split())
graph = [list(input()) for _ in range(n)]
word = list(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, l):
    if l == len(word):
        return 1
    if dp[x][y][l] != -1:
        return dp[x][y][l]

    dp[x][y][l] = 0
    for i in range(4):
        for j in range(1, k + 1):
            nx, ny = x + dx[i] * j, y + dy[i] * j
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == word[l]:
                dp[x][y][l] += dfs(nx, ny, l + 1)

    return dp[x][y][l]

dp = [[[-1] * len(word) for _ in range(m)] for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == word[0]:
            cnt += dfs(i, j, 1)

print(cnt)