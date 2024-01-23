from collections import Counter

def solution(topping):
    answer = 0

    a = Counter(topping)
    b = set()

    for i in topping:
        a[i] -= 1
        b.add(i)

        if a[i] == 0:
            a.pop(i)
        
        if len(a) == len(b):
            answer += 1

    return answer