import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
parent = list(map(int, input().split()))
d = int(input())

child = [[] for _ in range(n)]
root = 0
leaf = [0] * n

for i in range(n):
    if parent[i] == -1:
        root = i
    else:
        child[parent[i]].append(i)

def dfs(x):
    if len(child[x]) == 0:
        leaf[x] = 1
    for i in child[x]:
        dfs(i)
        leaf[x] += leaf[i]

for i in range(n):
    if d in child[i]:
        child[i].remove(d)

if root != d:
    dfs(root)

print(leaf[root])