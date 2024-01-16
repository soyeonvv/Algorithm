n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
calculation = [list(map(int, input().split())) for _ in range(k)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def calculate(order):
    a_copy = [row[:] for row in a]
    for i in order:
        r, c, s = calculation[i]
        for j in range(s, -1, -1):
            top_x, top_y = r - j - 1, c - j - 1
            bottom_x, bottom_y = r + j - 1, c + j - 1
            nx, ny = top_x, top_y
            temp = a_copy[nx][ny]

            for d in range(4):
                while True:
                    nx, ny = nx + dx[d], ny + dy[d]
                    if nx < top_x or nx > bottom_x or ny < top_y or ny > bottom_y:
                        nx, ny = nx - dx[d], ny - dy[d]
                        break
                    temp, a_copy[nx][ny] = a_copy[nx][ny], temp

    global answer
    for i in a_copy:
        answer = min(answer, sum(i))

def backtracking(order):
    if len(order) == k:
        calculate(order)
        return
    for i in range(k):
        if i not in order:
            order.append(i)
            backtracking(order)
            order.pop()

answer = int(1e9)
backtracking([])
print(answer)