def solution(storey):
    answer = 0

    while storey:
        left = storey % 10
        next = storey // 10 % 10

        if left > 5:
            answer += (10 - left)
            storey += 10
        elif left == 5:
            answer += 5
            storey += (10 if next >= 5 else 0)
        else:
            answer += left
            
        storey //= 10
    
    return answer