from collections import deque

def solution(tickets):
    answer = []
    tickets.sort(key=lambda x:(x[0], x[1]))
    
    queue = deque()
    queue.append((["ICN"], tickets))

    while queue:
        path, t = queue.popleft()

        if len(t) == 0:
            answer = path
            break

        idx = -1
        for i in range(len(t)):
            if t[i][0] == path[-1]:
                idx = i
                break
        
        if idx == -1:
            continue

        while idx < len(t) and t[idx][0] == path[-1]:
            queue.append((path + [t[idx][1]], t[:idx] + t[idx + 1:]))
            idx += 1

    return answer