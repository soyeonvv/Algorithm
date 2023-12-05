def solution(s):
    answer = []
    temp = []
    for i in s.split("},"):
        temp.append(i.replace("{", "").replace("}", "").split(","))
    temp.sort(key=len)

    for i in temp:
        for j in i:
            if j not in answer:
                answer.append(j)
    
    return list(map(int, answer))