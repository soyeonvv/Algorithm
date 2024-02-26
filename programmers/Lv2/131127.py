from collections import Counter

def solution(want, number, discount):
    answer = 0
    num = sum(number)
    wishlist = {}
    for i in range(len(want)):
        wishlist[want[i]] = number[i]

    for i in range(len(discount) - num + 1):
        cnt = 0
        candidate = Counter(discount[i:i + num])
        for key, value in wishlist.items():
            if candidate[key] == value:
                cnt += 1
        if cnt == len(want):
            answer += 1

    return answer