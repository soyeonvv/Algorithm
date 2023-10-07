t = int(input())

def dfs(depth):
    global answer
    if depth == 11:
        answer = max(answer, sum(result))
        return
    for i in range(11):
        if visited[i]:
            continue
        if stats[depth][i]:
            visited[i] = 1
            result.append(stats[depth][i])
            dfs(depth + 1)
            result.pop()
            visited[i] = 0

for _ in range(t):
    stats = [list(map(int, input().split())) for _ in range(11)]
    answer = 0
    result = []
    visited = [0] * 11
    dfs(0)
    print(answer)