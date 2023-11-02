n = int(input())
seat = [[-1] * n for _ in range(n)]
favors = [[] for _ in range(n ** 2 + 1)]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n ** 2):
    num, *favor = map(int, input().split())
    favors[num].extend(favor)

    candidate = []
    for x in range(n):
        for y in range(n):
            if seat[x][y] != -1:
                continue
            vacant, fav = 0, 0
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    if seat[nx][ny] == -1:
                        vacant += 1
                    if seat[nx][ny] in favor:
                        fav += 1
            candidate.append((fav, vacant, x, y))

    candidate.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
    seat[candidate[0][2]][candidate[0][3]] = num

# 만족도 계산
answer = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for d in range(4):
            nx, ny = i + dx[d], j + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if seat[nx][ny] in favors[seat[i][j]]:
                    cnt += 1

        if cnt != 0:
            answer += 10 ** (cnt - 1)

print(answer)