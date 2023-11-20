from itertools import permutations

def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False
        
        for j in range(len(banned_id[i])):
            if banned_id[i][j] == '*':
                continue
            if users[i][j] != banned_id[i][j]:
                return False
    
    return True

def solution(user_id, banned_id):
    answer = []

    for i in permutations(user_id, len(banned_id)):
        if not check(i, banned_id):
            continue
        else:
            i = set(i)
            if i not in answer:
                answer.append(i)
    
    return len(answer)