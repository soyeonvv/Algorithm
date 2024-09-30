import heapq

def solution(n, k, enemy):
    r = len(enemy)
    if k >= r:
        return r
    
    q = []
    answer, cnt = 0, 0
    for i in enemy:
        heapq.heappush(q, -i)
        cnt += i
        if cnt > n:
            if k == 0:
                return answer
            cnt += heapq.heappop(q)
            k -= 1
        answer += 1
            
    return answer