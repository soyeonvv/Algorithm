n = int(input())
beads = [0] * 5
dp = [[[[[[[-1] * 5 for _ in range(5)] for _ in range(11)] for _ in range(11)] for _ in range(11)] for _ in range(11)] for _ in range(11)]

for i in range(n):
    beads[i] = int(input())

def dfs(a, b, c, d, e, x, y):
    if a == 0 and b == 0 and c == 0 and d == 0 and e == 0:
        return 1
    
    cnt = dp[a][b][c][d][e][x][y]
    if cnt != -1:
        return cnt

    cnt = 0
    if a >= 1 and x != 0 and y != 0:
        cnt += dfs(a - 1, b, c, d, e, 0, x)
    if b >= 1 and x != 1 and y != 1:
        cnt += dfs(a, b - 1, c, d, e, 1, x)
    if c >= 1 and x != 2 and y != 2:
        cnt += dfs(a, b, c - 1, d, e, 2, x)
    if d >= 1 and x != 3 and y != 3:
        cnt += dfs(a, b, c, d - 1, e, 3, x)
    if e >= 1 and x != 4 and y != 4:
        cnt += dfs(a, b, c, d, e - 1, 4, x)

    dp[a][b][c][d][e][x][y] = cnt
    return cnt

print(dfs(beads[0], beads[1], beads[2], beads[3], beads[4], -1, -1))