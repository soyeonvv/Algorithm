n = int(input())
dp = [5001] * (n + 1)
dp[0] = 0
sugar = [3, 5]

for i in range(2):
    for j in range(sugar[i], n + 1):
        if dp[j - sugar[i]] != 5001:
            dp[j] = min(dp[j], dp[j - sugar[i]] + 1)

if dp[n] == 5001:
    print(-1)
else:
    print(dp[n])