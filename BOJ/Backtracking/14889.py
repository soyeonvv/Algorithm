def process():
    start, link = 0, 0
    for i in range(n):
        for j in range(i + 1, n):
            if pick[i] == 0 and pick[j] == 0:
                start += stats[i][j]
                start += stats[j][i]
            elif pick[i] == 1 and pick[j] == 1:
                link += stats[i][j]
                link += stats[j][i]
    global result
    result = min(result, abs(start - link))
    return result

def dfs(start, cnt):
    if cnt == n // 2:
        if process() == 0:
            print(result)
            exit(0)
        return
    for i in range(start, n):
        pick[i] = 1
        dfs(i + 1, cnt + 1)
        pick[i] = 0

n = int(input())
stats = [list(map(int, input().split())) for _ in range(n)]

result = int(1e9)
pick = [0] * 20
dfs(0, 0)
print(result)