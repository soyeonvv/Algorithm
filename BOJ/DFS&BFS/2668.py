n = int(input())
numbers = [0] + [int(input()) for _ in range(n)]
answer = []

def dfs(now, start):
    visited[now] = 1
    value = numbers[now]
    if visited[value] == 0:
        dfs(value, start)
    elif visited[value] and value == start:
        answer.append(value)

for i in range(1, n + 1):
    visited = [0] * (n + 1)
    dfs(i, i)

answer.sort()
print(len(answer))
for i in answer:
    print(i)