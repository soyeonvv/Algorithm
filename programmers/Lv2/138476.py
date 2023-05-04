from collections import Counter

def solution(k, tangerine):
    answer = 0
    count = Counter(tangerine).most_common()

    for i in count:
        k -= i[1]
        answer += 1

        if k <= 0:
            return answer
    
    return answer