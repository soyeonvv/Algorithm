import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
w = int(input())
pos = [[1, 1], [n, n]] + [list(map(int, input().split())) for _ in range(w)]
dp = [[-1] * (w + 2) for _ in range(w + 2)]

def solution(i, j):
    if i > w or j > w:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]

    next = max(i, j) + 1
    ni = solution(next, j) + abs(pos[next][0] - pos[i][0]) + abs(pos[next][1] - pos[i][1])
    nj = solution(i, next) + abs(pos[next][0] - pos[j][0]) + abs(pos[next][1] - pos[j][1])
    dp[i][j] = min(ni, nj)
    return dp[i][j]

def dfs(x, y):
    if x > w or y > w:
        return
    nz = max(x, y) + 1
    nx = abs(pos[nz][0] - pos[x][0]) + abs(pos[nz][1] - pos[x][1])
    ny = abs(pos[nz][0] - pos[y][0]) + abs(pos[nz][1] - pos[y][1])

    if dp[nz][y] + nx < dp[x][nz] + ny:
        print(1)
        dfs(nz, y)
    else:
        print(2)
        dfs(x, nz)
    return

print(solution(0, 1))
dfs(0, 1)