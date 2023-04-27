from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    discounts = [10, 20, 30, 40]

    for discount in product(discounts, repeat=len(emoticons)):
        plus = 0
        result = 0

        for user in users:
            cost = 0
            for i in range(len(discount)):
                if discount[i] >= user[0]:
                    cost += (emoticons[i] - (emoticons[i] * discount[i] / 100))
            if cost >= user[1]:
                plus += 1
            else:
                result += cost

        answer = max(answer, [plus, result])

    return answer