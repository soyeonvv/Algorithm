def solution(menu, order, k):
    answer = 0
    table = []

    for i in range(len(order)):
        if not table:
            table.append(i * k + menu[order[i]])
        else:
            temp = []
            for x in table:
                if x > i * k:
                    temp.append(x)
            if temp:
                temp.append(temp[-1] + menu[order[i]])
            else:
                temp.append(i * k + menu[order[i]])
            table = temp
        answer = max(answer, len(table))

    return answer