n = int(input())

child = []
dp = [1] * n

for _ in range(n):
    child.append(int(input()))

for i in range(n):
    for j in range(i):
        if child[j] < child[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))