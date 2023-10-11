def check(line):
    for i in range(n - 1):
        if abs(line[i] - line[i + 1]) > 1:
            return False
        if line[i] < line[i + 1]:
            for j in range(l):
                if i - j < 0 or line[i] != line[i - j] or used[i - j]:
                    return False
                if line[i] == line[i - j]:
                    used[i - j] = True
        elif line[i] > line[i + 1]:
            for j in range(l):
                if i + 1 + j >= n or line[i + 1] != line[i + 1 + j] or used[i + 1 + j]:
                    return False
                if line[i + 1] == line[i + 1 + j]:
                    used[i + 1 + j] = True

    return True

n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

for i in range(n):
    used = [False] * n
    if check(graph[i]):
        cnt += 1

for j in range(n):
    used = [False] * n
    if check([graph[i][j] for i in range(n)]):
        cnt += 1

print(cnt)