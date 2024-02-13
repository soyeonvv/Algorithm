n, m, h = map(int, input().split())
dp = [[1] + [0] * h for _ in range(n + 1)]
for i in range(1, n + 1):
    blocks = list(map(int, input().split()))
    dp[i] = dp[i - 1][:]
    for j in blocks:
        for k in range(j, h + 1):
            dp[i][k] += dp[i - 1][k - j]

print(dp[n][h] % 10007)