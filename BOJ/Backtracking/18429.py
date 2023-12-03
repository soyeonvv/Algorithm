n, k = map(int, input().split())
a = list(map(int, input().split()))

selected = []

def check(weight):
    for i in range(n):
        if weight - k + a[selected[i]] >= 500:
            weight = weight - k + a[selected[i]]
            continue
        else:
            return 0
    return 1

def dfs():
    global answer
    if len(selected) == n:
        answer += check(500)
        return
    for i in range(n):
        if i not in selected:
            selected.append(i)
            dfs()
            selected.pop()

answer = 0
dfs()
print(answer)