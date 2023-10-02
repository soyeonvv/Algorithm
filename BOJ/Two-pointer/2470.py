import sys
input = sys.stdin.readline

n = int(input())

num = list(map(int, input().split()))
num.sort()

l, r = 0, n - 1
best_sum = 1 << 31
v1, v2 = 0, 0

while l < r:
    s = num[l] + num[r]

    if abs(s) < best_sum:
        best_sum = abs(s)
        v1, v2 = num[l], num[r]

    if s > 0:
        r -= 1
    else:
        l += 1

print(v1, v2)