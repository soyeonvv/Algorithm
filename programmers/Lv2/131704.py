def solution(order):
    n = len(order)

    belt = []
    idx, cnt = 0, 0

    for i in range(1, n + 1):
        belt.append(i)

        while belt and belt[-1] == order[idx]:
            idx += 1
            cnt += 1
            belt.pop()

    return cnt