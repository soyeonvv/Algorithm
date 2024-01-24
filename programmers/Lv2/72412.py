from itertools import combinations
from collections import defaultdict

def solution(info, query):
    answer = []
    dic = defaultdict(list)
    for i in info:
        i = i.split()
        infos = i[:-1]
        score = int(i[-1])

        for n in range(5):
            case = list(combinations([0, 1, 2, 3], n))
            for c in case:
                tmp = infos[:]
                for idx in c:
                    tmp[idx] = '-'
                key = ''.join(tmp)
                dic[key].append(score)

    for value in dic.values():
        value.sort()
    
    for q in query:
        q = q.replace('and ', '').split()
        q_key = ''.join(q[:-1])
        q_score = int(q[-1])
        cnt = 0
        if q_key in dic:
            scores = dic[q_key]
            l, r = 0, len(scores) - 1
            while l <= r:
                mid = (l + r) // 2
                if scores[mid] >= q_score:
                    cnt += (r - mid + 1)
                    r = mid - 1
                else:
                    l = mid + 1
        answer.append(cnt)
                        
    return answer