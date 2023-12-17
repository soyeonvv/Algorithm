def solution(stones, k):
    answer = 0
    l, r = 1, max(stones)
    
    while l <= r:
        mid = (l + r) // 2
        cnt = 0
        for i in stones:
            if i - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt < k:
            l = mid + 1
        else:
            answer = mid
            r = mid - 1
        
    return answer