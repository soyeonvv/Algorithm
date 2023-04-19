from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    for dungeon in permutations(dungeons):
        fatigue = k
        cnt = 0
        for min_fatigue, cost in dungeon:
            if fatigue < min_fatigue:
                break
            else:
                cnt += 1
                fatigue -= cost
        answer = max(answer, cnt)
        
    return answer