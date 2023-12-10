INF = int(1e9)

C, N = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
dp = [0] + [INF] * C

for i in range(C):
    for m, n in info:
        if i + n < C:
            dp[i + n] = min(dp[i + n], dp[i] + m)
        else:
            dp[C] = min(dp[C], dp[i] + m)

print(dp[C])