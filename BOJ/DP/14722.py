n = int(input())
graph = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * 3 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        milk = graph[i][j]

        # 현재 위치: 딸기 우유
        if milk == 0:
            dp[i][j][0] = max(dp[i - 1][j][2] + 1, dp[i][j - 1][2] + 1)
        else:
            dp[i][j][0] = max(dp[i - 1][j][0], dp[i][j - 1][0])

        # 현재 위치: 초코 우유
        if milk == 1 and dp[i][j][0] > dp[i][j][1]:
            dp[i][j][1] = max(dp[i - 1][j][0] + 1, dp[i][j - 1][0] + 1)
        else:
            dp[i][j][1] = max(dp[i - 1][j][1], dp[i][j - 1][1])

        # 현재 위치: 바나나 우유
        if milk == 2 and dp[i][j][1] > dp[i][j][2]:
            dp[i][j][2] = max(dp[i - 1][j][1] + 1, dp[i][j - 1][1] + 1)
        else:
            dp[i][j][2] = max(dp[i - 1][j][2], dp[i][j - 1][2])

print(max(map(max, map(max, dp))))