answer = list(map(int, input().split()))
result = 0

def score(youngjae):
    s = 0
    for i in range(10):
        if youngjae[i] == answer[i]:
            s += 1
    return s

def dfs(x, y, youngjae):
    global result
    if len(youngjae) == 10:
        if score(youngjae) >= 5:
            result += 1
        return

    for i in range(1, 6):
        if x != 0 and x == y and i == x:
            continue
        else:
            youngjae.append(i)
            dfs(y, i, youngjae)
            youngjae.pop()

dfs(0, 0, [])
print(result)