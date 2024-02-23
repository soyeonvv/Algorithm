from itertools import combinations_with_replacement
import heapq

def solution(k, n, reqs):
    answer = int(1e9)
    
    comb = combinations_with_replacement([i for i in range(k)], n - k)
    # 가능한 유형-상담원 수 케이스 만들기
    case = []
    for i in comb:
        base = [1] * k
        for j in i:
            base[j] += 1
        case.append(base)

    # 유형별 시작 시간-종료 시간 테이블
    table = [[] for _ in range(k)]
    for a, b, c in reqs:
        table[c - 1].append((a, a + b))

    def get_time(waiting, cnt):
        time = 0
        q = []
        for _ in range(cnt):
            heapq.heappush(q, 0)
        for start, end in waiting:
            t = heapq.heappop(q)
            if start > t:
                heapq.heappush(q, end)
            else:
                time += t - start
                heapq.heappush(q, t - start + end)
        return time
    
    for i in case:
        time = 0
        for j in range(k):
            time += get_time(table[j], i[j])
        answer = min(answer, time)

    return answer