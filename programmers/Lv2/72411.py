from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    for i in course:
        dic = defaultdict(int)
        for order in orders:
            case = (combinations(list(order), i))
            for c in case:
                key = "".join(sorted(c))
                dic[key] += 1

        max_order = [k for k,v in dic.items() if (v == max(dic.values()) and v >= 2)]
        answer.extend(max_order)
        
    answer.sort()
    return answer