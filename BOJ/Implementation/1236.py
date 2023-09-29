n, m = map(int, input().split())

castle = [list(input()) for _ in range(n)]

row = [0] * n
col = [0] * m

for i in range(n):
    for j in range(m):
        if castle[i][j] == 'X':
            row[i] = 1
            col[j] = 1

rowCount = n
colCount = m
rowCount -= row.count(1)
colCount -= col.count(1)

print(max(rowCount, colCount))