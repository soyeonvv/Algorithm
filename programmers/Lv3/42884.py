def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])

    cctv = -30001

    for r in routes:
        s = r[0]
        if s <= cctv:
            continue
        answer += 1
        cctv = r[1]
    return answer