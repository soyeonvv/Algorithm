from itertools import combinations
INF = int(1e9)

def check(flower):
    global answer
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = []
    cost = 0
    for x, y in flower:
        visited.append((x, y))
        cost += garden[x][y]

        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            
            if (nx, ny) not in visited:
                visited.append((nx, ny))
                cost += garden[nx][ny]
            else:
                return
            
    answer = min(answer, cost)

n = int(input())

garden = [list(map(int, input().split())) for _ in range(n)]
pos = [(x, y) for x in range(1, n - 1) for y in range(1, n - 1)]

answer = INF

for flower in combinations(pos, 3):
    check(flower)

print(answer)