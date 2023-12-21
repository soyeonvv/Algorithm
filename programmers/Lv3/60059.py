def rotate(key):
    key = list(map(list, zip(*key[::-1])))
    return key

def check(board, m, n):
    for i in range(m - 1, m - 1 + n):
        for j in range(m - 1, m - 1 + n):
            if board[i][j] != 1:
                return False
    return True

def solution(key, lock):
    m, n = len(key), len(lock)
    board = [[0] * (m * 2 + n - 2) for _ in range(m * 2 + n - 2)]

    for i in range(m - 1, m - 1 + n):
        for j in range(m - 1, m - 1 + n):
            board[i][j] = lock[i - (m - 1)][j - (m - 1)]

    if check(board, m, n):
        return True

    for i in range(m - 1 + n):
        for j in range(m - 1 + n):
            for _ in range(4):
                temp = [x[:] for x in board]
                for k in range(m):
                    for l in range(m):
                        temp[k + i][l + j] += key[k][l]
                        if temp[k + i][l + j] >= 2:
                            continue
                        if check(temp, m, n):
                            return True
                key = rotate(key)
    return False