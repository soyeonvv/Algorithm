import sys
from itertools import combinations
input = sys.stdin.readline

game = list(combinations(range(6), 2))
answer = []

def dfs(depth):
    global ans
    if depth == 15:
        ans = 1
        for i in score:
            if i.count(0) != 3:
                ans = 0
                break
        return
    
    g1, g2 = game[depth]
    for x, y in ((0, 2), (1, 1), (2, 0)):
        if score[g1][x] > 0 and score[g2][y] > 0:
            score[g1][x] -= 1
            score[g2][y] -= 1
            dfs(depth + 1)
            score[g1][x] += 1
            score[g2][y] += 1

for _ in range(4):
    data = list(map(int, input().split()))
    score = [data[i:i + 3] for i in range(0, 16, 3)]
    ans = 0
    dfs(0)
    answer.append(ans)

for i in answer:
    print(i, end=' ')