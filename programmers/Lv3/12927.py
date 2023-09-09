import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    answer = 0
    
    q = []
    for work in works:
        heapq.heappush(q, -work)

    while n > 0:
        heapq.heappush(q, heapq.heappop(q) + 1)
        n -= 1

    for i in q:
        answer += i ** 2

    return answer