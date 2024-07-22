def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    # 여벌 체육복을 가져온 학생이 도난당한 경우
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)

    for i in reserve:
        if i - 1 in lost:
            lost.remove(i - 1)
        elif i + 1 in lost:
            lost.remove(i + 1)
            
    answer = n - len(lost)
    return answer