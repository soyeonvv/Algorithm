import heapq

def solution(scoville, K):
    answer = 0

    scoville.sort()
    while scoville[0] < K:
        if len(scoville) == 1:
            answer = -1
            break
        x, y = heapq.heappop(scoville), heapq.heappop(scoville)
        new = x + y * 2
        heapq.heappush(scoville, new)
        answer += 1
            
    return answer