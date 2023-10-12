N, M, K = map(int, input().split())
fireballs = []
for _ in range(M):
    i_r, i_c, i_m, i_s, i_d = list(map(int, input().split()))
    fireballs.append([i_r - 1, i_c - 1, i_m, i_s, i_d])

graph = [[[] for _ in range(N + 1)] for _ in range(N + 1)]

direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for _ in range(K):
    while fireballs:
        r, c, m, s, d = fireballs.pop(0)
        nr = (r + s * direction[d][0]) % N
        nc = (c + s * direction[d][1]) % N
        graph[nr][nc].append([m, s, d])

    for i in range(N):
        for j in range(N):
            if len(graph[i][j]) > 1:
                sum_m, sum_s, odd, even, cnt = 0, 0, 0, 0, len(graph[i][j])
                while graph[i][j]:
                    mm, ss, dd = graph[i][j].pop(0)
                    sum_m += mm
                    sum_s += ss
                    if dd % 2 != 0:
                        odd += 1
                    else:
                        even += 1
                if odd == cnt or even == cnt:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                if sum_m // 5 != 0:
                    for x in nd:
                        fireballs.append([i, j, sum_m // 5, sum_s // cnt, x])

            if len(graph[i][j]) == 1:
                fireballs.append([i, j] + graph[i][j].pop())

answer = 0
for fireball in fireballs:
    answer += fireball[2]
print(answer)