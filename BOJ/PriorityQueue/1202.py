import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

jewels.sort(key=lambda x:(x[0], -x[1]))
bags.sort()

answer = 0
q = []
for i in bags:
    while jewels and i >= jewels[0][0]:
        heapq.heappush(q, -jewels[0][1])
        heapq.heappop(jewels)
    if q:
        answer -= heapq.heappop(q)

print(answer)