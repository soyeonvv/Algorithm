k, n, f = map(int, input().split())
friends = [[] for _ in range(n + 1)]
for _ in range(f):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

def dfs(x, answer):
    if len(answer) == k:
        for i in answer:
            print(i)
        exit(0)
    for i in range(x + 1, n + 1):
        if visited[i] == 0:
            for j in answer:
                if j not in friends[i]:
                    break
            else:
                visited[i] = 1
                dfs(i, answer + [i])

for i in range(1, n + 1):
    visited = [0] * (n + 1)
    visited[i] = 1
    dfs(i, [i])

print(-1)