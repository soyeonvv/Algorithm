n, m = map(int, input().split())

chess = [list(input()) for _ in range(n)]
count = []

for i in range(n - 7):
    for j in range(m - 7):
        w = 0
        b = 0

        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if chess[k][l] != 'B':
                        b += 1
                    if chess[k][l] != 'W':
                        w += 1
                else:
                    if chess[k][l] != 'B':
                        w += 1
                    if chess[k][l] != 'W':
                        b += 1
        count.append(min(w, b))

print(min(count))