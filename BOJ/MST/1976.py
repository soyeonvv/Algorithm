n = int(input())
m = int(input())

parent = [i for i in range(n)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a, b= find_parent(a), find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(n):
    link = list(map(int, input().split()))
    for j in range(n):
        if link[j] == 1:
            union_parent(i, j)

plan = list(map(int, input().split()))
parent_city = find_parent(plan[0] - 1)
for i in range(1, m):
    if find_parent(plan[i] - 1) != parent_city:
        print('NO')
        break
else:
    print('YES')