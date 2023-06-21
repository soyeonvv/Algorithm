from collections import Counter

def solution(weights):
    answer = 0
    # 1:1
    counter = Counter(weights)
    for i in counter.values():
        if i >= 2:
            answer += i * (i - 1) // 2
    
    weights = list(set(weights))
            
    for w in weights:
    # 1:2
        if w * 1 / 2 in weights:
            answer += counter[w * 1 / 2] * counter[w]
    # 2:3
        if w * 2 / 3 in weights:
            answer += counter[w * 2 / 3] * counter[w]
    # 3:4
        if w * 3 / 4 in weights:
            answer += counter[w * 3 / 4] * counter[w]
    
    return answer