def solution(N, number):
    answer = -1
    dp = []
    
    for i in range(1, 9):
        case = set()
        case.add(int(str(N) * i))
        for j in range(i - 1):
            for a in dp[j]:
                for b in dp[-j - 1]:
                    case.add(a + b)
                    case.add(a - b)
                    case.add(a * b)
                    if b != 0:
                        case.add(a // b)
                        
        if number in case:
            answer = i
            break
            
        dp.append(case)
            
    return answer