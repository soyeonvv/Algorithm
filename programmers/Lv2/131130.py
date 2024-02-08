def solution(cards):
    answer = []
    visited = [0] * (len(cards) + 1)
    
    for i in cards:
        if visited[i] == 0:
            group = []
            while i not in group:
                group.append(i)
                i = cards[i - 1]
                visited[i] = 1
            answer.append(len(group))
    
    if answer[0] == len(cards):
        return 0
    else:
        answer.sort(reverse=True)
    
    return answer[0] * answer[1]