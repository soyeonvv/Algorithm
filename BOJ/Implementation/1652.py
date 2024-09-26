n = int(input())
graph = [list(input()) for _ in range(n)]
a, b = 0, 0

for i in range(n):
    cntA, cntB = 0, 0
    A, B = [], []

    for j in range(n):
        if graph[i][j] == '.':
            cntA += 1
        else:
            A.append(cntA)
            cntA = 0
        if graph[j][i] == '.':
            cntB += 1
        else:
            B.append(cntB)
            cntB = 0
    A.append(cntA)
    B.append(cntB)

    a += sum(x >= 2 for x in A)
    b += sum(x >= 2 for x in B)
    
print(a, b)