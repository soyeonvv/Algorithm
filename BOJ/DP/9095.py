t = int(input())

dp = [1, 2, 4]

for i in range(3, 10):
    dp.append(sum(dp[i -3:i]))

for _ in range(t):
    n = int(input())
    print(dp[n - 1])