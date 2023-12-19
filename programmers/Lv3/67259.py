from collections import deque
INF = int(1e9)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solution(board):
    n = len(board)
    queue = deque()
    dp = [[[INF] * n for _ in range(n)] for _ in range(4)]

    for i in range(4):
        dp[i][0][0] = 0
    if board[0][1] == 0:
        queue.append((0, 1, 0, 100))
        dp[0][0][1] = 100
    if board[1][0] == 0:
        queue.append((1, 0, 1, 100))
        dp[1][1][0] = 100

    while queue:
        x, y, d, c = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                cost = c + 100 if i == d else c + 600
                if dp[i][nx][ny] > cost:
                    dp[i][nx][ny] = cost
                    queue.append((nx, ny, i, cost))

    return min([dp[i][n - 1][n - 1] for i in range(4)])