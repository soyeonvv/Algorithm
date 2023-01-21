t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    dp = [x for x in range(1, n + 1)]
    for _ in range(k):
        for i in range(1, n):
            dp[i] += dp[i - 1]
    print(dp[n - 1])