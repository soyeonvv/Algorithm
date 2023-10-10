from collections import deque

n = int(input())
k = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1

l = int(input())
change = {}

for _ in range(l):
    a, b = input().split()
    change[int(a)] = b

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우, 하, 좌, 상

x, y = 1, 1
time = 0
d = 0

queue = deque()

while True:
    queue.append((x, y))

    x += direction[d][0]
    y += direction[d][1]

    time += 1

    if x < 1 or x > n or y < 1 or y > n or graph[x][y] == 2:
        break
    if not graph[x][y]:
        i, j = queue.popleft()
        graph[i][j] = 0

    graph[x][y] = 2

    if time in change:
        if change[time] == 'D':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4

print(time)