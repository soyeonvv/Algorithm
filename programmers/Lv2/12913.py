def solution(land):
    n = len(land)
    
    dp = [row[:] for row in land]
    for i in range(1, n):
        for j in range(4):
            dp[i][j] = land[i][j] + max([x for idx, x in enumerate(dp[i - 1]) if idx != j]) 

    return max(dp[n - 1])