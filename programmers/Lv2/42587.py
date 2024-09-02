def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = []

    while queue:
        flag = 0
        idx, p = queue.pop(0)
        for x, y in queue:
            if y > p:
                queue.append((idx, p))
                flag = 1
                break
        if flag:
            continue
        answer.append(idx)

    return answer.index(location) + 1