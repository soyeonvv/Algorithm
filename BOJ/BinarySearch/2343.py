import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

left = max(data)
right = sum(data)

while left <= right:
    mid = (left + right) // 2
    total = 0
    cnt = 1
    for i in data:
        if total + i > mid:
            cnt += 1
            total = 0
        total += i

    if cnt <= m:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)