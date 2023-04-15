n = int(input())
array = [0] * (n + 1)
dp = [0] * (n + 1)

scores = list(map(int, input().split()))

for i in range(1, n + 1):
    max_val, min_val = 0, 10001
    array[i] = scores[i - 1]

    for j in range(i, 0, -1):
        max_val = max(max_val, array[j])
        min_val = min(min_val, array[j])
        dp[i] = max(dp[i], max_val - min_val + dp[j - 1])

print(dp[n])