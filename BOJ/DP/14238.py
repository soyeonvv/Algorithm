from collections import Counter

work = list(input())
n = len(work)
cnt = Counter(work)
answer = [''] * n
dp = [[[[[False] * 3 for _ in range(3)] for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]

def dfs(a, b, c, x, y):
    if a == 0 and b == 0 and c == 0:
        print(*answer, sep='')
        exit(0)

    # 이미 탐색한 경우
    if dp[a][b][c][x][y]:
        return False

    dp[a][b][c][x][y] = True

    if a >= 1:
        answer[n - (a + b + c)] = 'A'
        if dfs(a - 1, b , c, 0, x):
            return True
    if b >= 1:
        answer[n - (a + b + c)] = 'B'
        if x != 1:
            if dfs(a, b - 1, c, 1, x):
                return True
    if c >= 1:
        answer[n - (a + b + c)] = 'C'
        if x != 2 and y != 2:
            if dfs(a, b, c - 1, 2, x):
                return True

    return False

dfs(cnt['A'], cnt['B'], cnt['C'], -1, -1)
print(-1)