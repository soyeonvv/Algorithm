import sys
input = sys.stdin.readline

n, s = map(int, input().split())

num = list(map(int, input().split()))
num.insert(0, 0)

sum, r = 0, 0
answer = n + 1

for l in range(1, n + 1):
    sum -= num[l - 1]

    while (r + 1 <= n and sum < s):
        r += 1
        sum += num[r]

    if sum >= s:
        answer = min(answer, r - l + 1)

if answer == n + 1:
    answer = 0

print(answer)