n = int(input())
selected = [0 for _ in range(n)]
ans = 0

def check(r1, c1, r2, c2):
    if c1 == c2:
        return True
    if r1 - c1 == r2 - c2:
        return True
    if r1 + c1 == r2 + c2:
        return True
    return False

def dfs(k):
    if k == n:
        global ans
        ans += 1
    else:
        for i in range(n):
            possible = True
            for j in range(k):
                if check(k, i, j, selected[j]):
                    possible = False
                    break
            if possible:
                selected[k] = i
                dfs(k + 1)
                selected[k] = 0

dfs(0)
print(ans)