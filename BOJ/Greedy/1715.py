import heapq

n = int(input())
card = []

for _ in range(n):
    heapq.heappush(card, int(input()))

if len(card) == 1:
    print(0)
else:
    result = 0
    while len(card) > 1:
        x = heapq.heappop(card)
        y = heapq.heappop(card)
        result += x + y
        heapq.heappush(card, x + y)

    print(result)