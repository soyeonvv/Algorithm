def dfs(start, graph, visited, link):
    cnt = 1
    visited[start] = True

    for i in graph[start]:
        if visited[i] == False and link[start][i]:
            cnt += dfs(i, graph, visited, link)

    return cnt

def solution(n, wires):
    answer = int(1e9)
    graph = [[] for _ in range(n + 1)]
    link = [[True] * (n + 1) for _ in range(n + 1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in wires:
        visited = [False] * (n + 1)

        link[a][b] = False
        cntA = dfs(a, graph, visited, link)
        cntB = dfs(b, graph, visited, link)
        link[a][b] = True

        answer = min(answer, abs(cntA - cntB))

    return answer