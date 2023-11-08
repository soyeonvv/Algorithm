n, l, r, x = map(int, input().split())
level = list(map(int, input().split()))
level.sort()
answer = 0

def dfs(depth, idx, high, low, total):
    global answer
    if total > r:
        return
    elif depth >= 2 and l <= total <= r:
        if high - low >= x and not(high == None or low == None):
            answer += 1
    for i in range(idx, len(level)):
        if low == None:
            dfs(depth + 1, i + 1, level[i], level[i], total + level[i])
        else:
            dfs(depth + 1, i + 1, level[i], low, total + level[i])

dfs(0, 0, None, None, 0)
print(answer)