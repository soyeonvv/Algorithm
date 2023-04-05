def solution(brown, yellow):

    x = int(brown / 2) + 2
    y = 0

    while (x - 2) * (y - 2) != yellow:
        x -= 1
        y += 1
    
    answer = [x, y]

    return answer