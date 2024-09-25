import sys
import heapq

left, right = [], []
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())

    if not left or -left[0] >= n:
        heapq.heappush(left, -n)
    else:
        heapq.heappush(right, n)

    if len(left) > len(right) + 1:
        heapq.heappush(right, -heapq.heappop(left))
    elif len(right) > len(left):
        heapq.heappush(left, -heapq.heappop(right))

    print(-left[0])