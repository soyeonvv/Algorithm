n = int(input())
buildings = list(map(int, input().split()))
answer = [0] * n

for i in range(n - 1):
    incline = -int(1e9)
    for j in range(i + 1, n):
        v = (buildings[j] - buildings[i]) / (j - i)
        if v <= incline:
            continue
        incline = max(incline, v)
        answer[i] += 1
        answer[j] += 1

print(max(answer))