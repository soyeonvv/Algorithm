n, t = map(int, input().split())
table = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (t + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, t + 1):
        if table[i][0] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - table[i][0]] + table[i][1])

print(dp[n][t])