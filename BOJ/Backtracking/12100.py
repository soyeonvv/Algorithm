import sys
import copy
input = sys.stdin.readline

def left(graph):
    for i in range(n):
        p = 0
        for j in range(1, n):
            if graph[i][j]:
                temp = graph[i][j]
                graph[i][j] = 0

                if graph[i][p] == 0:
                    graph[i][p] = temp
                elif graph[i][p] == temp:
                    graph[i][p] *= 2
                    p += 1
                else:
                    p += 1
                    graph[i][p] = temp
    return graph


def right(graph):
    for i in range(n):
        p = n - 1
        for j in range(n - 2, -1, -1):
            if graph[i][j]:
                temp = graph[i][j]
                graph[i][j] = 0

                if graph[i][p] == 0:
                    graph[i][p] = temp
                elif graph[i][p] == temp:
                    graph[i][p] *= 2
                    p -= 1
                else:
                    p -= 1
                    graph[i][p] = temp
    return graph

def up(graph):
    for j in range(n):
        p = 0
        for i in range(1, n):
            if graph[i][j]:
                temp = graph[i][j]
                graph[i][j] = 0

                if graph[p][j] == 0:
                    graph[p][j] = temp
                elif graph[p][j] == temp:
                    graph[p][j] *= 2
                    p += 1
                else:
                    p += 1
                    graph[p][j] = temp
    return graph


def down(graph):
    for j in range(n):
        p = n - 1
        for i in range(n - 2, -1, -1):
            if graph[i][j]:
                temp = graph[i][j]
                graph[i][j] = 0

                if graph[p][j] == 0:
                    graph[p][j] = temp
                elif graph[p][j] == temp:
                    graph[p][j] *= 2
                    p -= 1
                else:
                    p -= 1
                    graph[p][j] = temp
    return graph

def dfs(depth, graph):
    global answer
    if depth == 5:
        answer = max(answer, max(map(max, graph)))
        return

    for i in range(4):
        c_graph = copy.deepcopy(graph)
        if i == 0:
            dfs(depth + 1, left(c_graph))
        elif i == 1:
            dfs(depth + 1, right(c_graph))
        elif i == 2:
            dfs(depth + 1, up(c_graph))
        else:
            dfs(depth + 1, down(c_graph))

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

answer = 0
dfs(0, graph)
print(answer)