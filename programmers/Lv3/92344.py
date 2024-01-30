def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])
    temp = [[0] * (m + 1) for _ in range(n + 1)]
    for t, r1, c1, r2, c2, degree in skill:
        temp[r1][c1] += degree if t == 2 else -degree
        temp[r1][c2 + 1] += degree if t == 1 else -degree
        temp[r2 + 1][c1] += degree if t == 1 else -degree
        temp[r2 + 1][c2 + 1] += degree if t == 2 else -degree

    for i in range(n):
        for j in range(m):
            temp[i][j + 1] += temp[i][j]

    for i in range(n):
        for j in range(m):
            temp[i + 1][j] += temp[i][j]

    for i in range(n):
        for j in range(m):
            board[i][j] += temp[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer