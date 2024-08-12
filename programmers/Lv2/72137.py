answer = 0

def dfs(cnt, result, ability, check):
    global answer
    n, m = len(ability), len(ability[0])
    
    if cnt == m:
        answer = max(answer, result)
        return
        
    for i in range(n):
        if check[i] == 0:
            check[i] = 1
            dfs(cnt + 1, result + ability[i][cnt], ability, check)
            check[i] = 0

def solution(ability):   
    check = [0] * len(ability)
    
    dfs(0, 0, ability, check)
    return answer