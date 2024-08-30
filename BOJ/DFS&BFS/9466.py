import sys
sys.setrecursionlimit(10**6)

t = int(input())

def dfs(now):
    global result
    visited[now] = 1
    cycle.append(now)
    num = students[now]

    if visited[num]:
        if num in cycle:
            result += cycle[cycle.index(num):]
        return
    else:
        dfs(num)

for _ in range(t):
    n = int(input())
    students = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)
    result = []

    for i in range(1, n + 1):
        if visited[i] == 0:
            cycle = []
            dfs(i)

    print(n - len(result))