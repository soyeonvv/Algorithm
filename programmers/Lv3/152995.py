def solution(scores):
    answer = 1
    wanho = scores[0]

    scores.sort(key=lambda x:(-x[0], x[1]))

    temp = 0
    for score in scores:
        if wanho[0] < score[0] and wanho[1] < score[1]:
            answer = -1
            break

        if temp <= score[1]:
            if sum(wanho) < sum(score):
                answer += 1
            temp = score[1]

    return answer