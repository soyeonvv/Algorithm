# DFS
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

r, c = map(int, input().split())

graph = [list(map(str, input().rstrip())) for _ in range(r)]
count = 0
directions = [(-1, -1), (-1, 0), (-1, 1)]

def dfs(x, y):
    global count
    if x == 0:
        count += 1
        return True
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx and 0 <= ny < r:
            if graph[ny][nx] == '.':
                graph[ny][nx] = 'x'
                if dfs(nx, ny):
                    return True

    return False

for y in range(r):
    dfs(c -1, y)

print(count)