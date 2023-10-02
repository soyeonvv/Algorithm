import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = []

for _ in range(n):
    house.append(int(input()))

def determination(d):
    cnt, last = 1, house[0]
    for i in range(1, n):
        if house[i] - last < d: continue
        last = house[i]
        cnt += 1
    return cnt >= c

house.sort()
l, r, answer = 1, 1000000000, 0
while l <= r:
    mid = (l + r) // 2
    if determination(mid):
        answer = mid
        l = mid + 1
    else:
        r = mid - 1

print(answer)