n, m = map(int, input().split())

dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, m):
    dp[0][i] += dp[0][i - 1]

for i in range(1, n):
    # 임시 배열
    left = dp[i][:]
    right = dp[i][:]

    # →
    for j in range(m):
        if j == 0:
            left[j] += dp[i - 1][j]
        else:
            left[j] += max(dp[i - 1][j], left[j - 1])

    # ←
    for j in range(m - 1, -1, -1):
        if j == m - 1:
            right[j] += dp[i - 1][j]
        else:
            right[j] += max(dp[i - 1][j], right[j + 1])

    for j in range(m):
        dp[i][j] = max(left[j], right[j])

print(dp[n - 1][m - 1])