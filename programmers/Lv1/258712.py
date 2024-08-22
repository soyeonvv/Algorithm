def solution(friends, gifts):
    n = len(friends)
    graph = [[0] * n for _ in range(n)]
    for i in gifts:
        x, y = i.split()
        graph[friends.index(x)][friends.index(y)] += 1

    table = [[0] * 3 for _ in range(n)]
    for i in range(n):
        table[i][0] = sum(graph[i][:])
        for j in range(n):
            table[i][1] += graph[j][i]
        table[i][2] = table[i][0] - table[i][1]

    answer = [0] * n
    for i in range(n - 1):
        for j in range(i + 1, n):
            if graph[i][j] == graph[j][i]:
                if table[i][2] == table[j][2]:
                    continue
                elif table[i][2] > table[j][2]:
                    answer[i] += 1
                else:
                    answer[j] += 1
            elif graph[i][j] > graph[j][i]:
                answer[i] += 1
            else:
                answer[j] += 1

    return max(answer)