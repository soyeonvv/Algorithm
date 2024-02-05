def solution(s):
    answer = int(1e9)
    n = len(s)
    
    if n == 1:
        return 1
    
    for i in range(1, n // 2 + 1):
        z = ''
        cnt = 1
        temp = s[:i]
        
        for j in range(i, n, i):
            if temp == s[j:j + i]:
                cnt += 1
            else:
                if cnt == 1:
                    z += temp
                else:
                    z += (str(cnt) + temp)
                temp = s[j:j + i]
                cnt = 1
        if cnt == 1:
            z += temp
        else:
            z += (str(cnt) + temp)
            
        answer = min(answer, len(z))
    return answer