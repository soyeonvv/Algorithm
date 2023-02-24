n = int(input())

array = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 1)

for i in range(n):
    for j in range(i + array[i][0], n + 1):
        if dp[j] < dp[i] + array[i][1]:
            dp[j] = dp[i] + array[i][1]

print(dp[n])