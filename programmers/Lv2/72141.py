import heapq

def solution(ability, number):
    q = []
    for i in ability:
        heapq.heappush(q, i)
    
    for _ in range(number):
        a, b = heapq.heappop(q), heapq.heappop(q)
        for _ in range(2):
            heapq.heappush(q, a + b)
    
    return sum(q)