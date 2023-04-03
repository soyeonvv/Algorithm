from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    queue = deque(people)

    while queue:
        if len(queue) == 1:
            answer += 1
            break
        elif queue[0] + queue[-1] <= limit:
            answer += 1
            queue.pop()
            queue.popleft()
        else:
            answer += 1
            queue.pop()

    return answer