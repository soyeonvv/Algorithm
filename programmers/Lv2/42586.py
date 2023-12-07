import math

def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))

    value = days[0]
    cnt = 1
    for i in range(1, len(days)):
        if value >= days[i]:
            cnt += 1
        else:
            answer.append(cnt)
            value = days[i]
            cnt = 1

        if i == len(days) - 1:
            answer.append(cnt)
    
    return answer