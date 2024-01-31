t, w = map(int, input().split())
tree = [0] + [int(input()) for _ in range(t)]

dp = [[0] * (w + 1) for _ in range(t + 1)]
dp[1][0], dp[1][1] = tree[1] % 2, tree[1] // 2

for i in range(2, t + 1):
    for j in range(w + 1):
        n = tree[i] % 2 if j % 2 == 0 else tree[i] // 2
        dp[i][j] = max(dp[i - 1][:j + 1]) + n

print(max(dp[t]))