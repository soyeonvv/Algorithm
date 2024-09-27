n, k = map(int, input().split())
ice = [0] * 1000001
for _ in range(n):
    g, x = map(int, input().split())
    ice[x] = g

next = 2 * k + 1
window = sum(ice[:next])
answer = window

for i in range(next, 1000001):
    window += (ice[i] - ice[i - next])
    answer = max(answer, window)

print(answer)