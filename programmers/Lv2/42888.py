def solution(record):
    answer = []
    user = {}
    
    for i in record:
        if 'Enter' in i or 'Change' in i:
            x, id, nickname = i.split()
            user[id] = nickname
            
    for i in record:
        if 'Leave' in i:
            x, id = i.split()
            answer.append(user[id] + "님이 나갔습니다.")
        else:
            x, id, nickname = i.split()
            if x == 'Enter':
                answer.append(user[id] + "님이 들어왔습니다.")
            
    return answer