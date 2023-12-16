def solution(gems):
    n = len(gems)
    answer = [0, n]
    cnt = len(set(gems))
    dic = {gems[0]:1}
    l, r = 0, 0

    while l < n and r < n:
        if len(dic) < cnt:
            r += 1
            if r == n:
                break
            dic[gems[r]] = dic.get(gems[r], 0) + 1
        else:
            if (r - l) < answer[1] - answer[0]:
                answer = [l + 1, r + 1]
            if dic[gems[l]] == 1:
                del dic[gems[l]]
            else:
                dic[gems[l]] -= 1
            l += 1

    return answer