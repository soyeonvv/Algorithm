from collections import deque

def solution(x, y, n):
    queue = deque()
    queue.append((y, 0))
    
    if x == y:
        return 0
    
    while queue:
        value, cnt = queue.popleft()
        if value == x:
            return cnt
        if value > x:
            queue.append((value - n, cnt + 1))
            if value % 2 == 0:
                queue.append((value // 2, cnt + 1))
            if value % 3 == 0:
                queue.append((value // 3, cnt + 1))
    
    return -1