from collections import deque

def rotate_right(n):
     graph[n] = [graph[n][-1]] + graph[n][:-1]
def rotate_left(n):
    graph[n] = graph[n][1:] + [graph[n][0]]

graph = [list(map(int, input())) for _ in range(4)]
k = int(input())

for _ in range(k):
    x, d = map(int, input().split())
    x -= 1

    visited = [False] * 4
    visited[x] = True

    queue = deque()
    queue.append((x, d))
    rotate = deque()
    rotate.append((x, d))

    while queue:
        num, direction = queue.popleft()

        # 왼쪽 비교
        if num - 1 >= 0:
            if graph[num][6] != graph[num - 1][2] and not visited[num - 1]:
                visited[num - 1] = True
                rotate.append((num - 1, direction * (-1)))
                queue.append((num - 1, direction * (-1)))

        # 오른쪽 비교
        if num + 1 < 4:
            if graph[num][2] != graph[num + 1][6] and not visited[num + 1]:
                visited[num + 1] = True
                rotate.append((num + 1, direction * (-1)))
                queue.append((num + 1, direction * (-1)))

    while rotate:
        n, r = rotate.popleft()
        if r == 1:
            rotate_right(n)
        else:
            rotate_left(n)

answer = 0

for i in range(4):
    if graph[i][0] == 1:
        answer += 2 ** i

print(answer)