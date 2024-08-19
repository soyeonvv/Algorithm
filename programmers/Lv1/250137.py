def solution(bandage, health, attacks):
    attack = attacks.pop(0)
    h, cnt = health, 0
    
    for i in range(1, attacks[-1][0] + 1):
        cnt += 1
        if i == attack[0]:
            health -= attack[1]
            cnt = 0
            if health <= 0:
                return -1
            if attacks:
                attack = attacks.pop(0)
            continue
        
        if cnt == bandage[0]:
            health += sum(bandage[1:])
            cnt = 0
        else:
            health += bandage[1]
        
        if health > h:
            health = h
            
    return health