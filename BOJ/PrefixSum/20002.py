n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

sum_graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        sum_graph[i][j] = graph[i - 1][j - 1] + sum_graph[i - 1][j] + sum_graph[i][j - 1] - sum_graph[i - 1][j - 1]

answer = int(-1e9)
for k in range(n):
    for i in range(n - k):
        for j in range(n - k):
            value = sum_graph[i + k + 1][j + k + 1] - sum_graph[i + k + 1][j] - sum_graph[i][j + k + 1] + sum_graph[i][j]
            answer = max(answer, value)

print(answer)