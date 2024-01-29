def erase(m, n, board):
    blocks = set()
    cnt = 0
    for i in range(m - 1):
        for j in range(n - 1):
            # 2x2 블록 확인
            if board[i][j] != 0:
                if board[i][j] == board[i][j + 1] and board[i][j] == board[i + 1][j] and board[i][j] == board[i + 1][j + 1]:
                    for x in range(2):
                        for y in range(2):
                            blocks.add((i + x, j + y))
    for x, y in list(blocks):
        cnt += 1
        board[x][y] = 0

    return cnt, board

def move(m, n, board):
    for i in range(m - 1, -1, -1):
        for j in range(n):
            if board[i][j] != 0:
                p = i
                while p + 1 < m and board[p + 1][j] == 0:
                    board[p + 1][j] = board[p][j]
                    board[p][j] = 0
                    p += 1

    return board


def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board]

    while True:
        # 블록 삭제
        cnt, graph = erase(m, n, board)
        if cnt == 0:
            break
        answer += cnt
        # 블록 이동
        board = move(m, n, graph)

    return answer