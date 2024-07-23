def solution(picks, minerals):
    # 광물 수 > 캘 수 있는 광물 수
    pick_num = 0
    for i in picks:
        pick_num += i

    pick_num *= 5
    if len(minerals) > pick_num:
        minerals = minerals[:pick_num]

    fatigue = [{'diamond': 1, 'iron': 1, 'stone': 1},
               {'diamond': 5, 'iron': 1, 'stone': 1},
               {'diamond': 25, 'iron': 5, 'stone': 1}]

    new_minerals = []
    for i in range(0, len(minerals), 5):
        if i + 5 <= len(minerals):
            new_minerals.append(minerals[i:i + 5])
        else:
            new_minerals.append(minerals[i:])
        new_minerals[-1].insert(0, new_minerals[-1].count('stone'))
        new_minerals[-1].insert(0, new_minerals[-1].count('iron'))
        new_minerals[-1].insert(0, new_minerals[-1].count('diamond'))

    new_minerals.sort(key=lambda x:(-x[0], -x[1], -x[2]))

    answer = 0
    for i, pick in enumerate(picks):
        while pick > 0 and new_minerals:
            for mineral in new_minerals.pop(0):
                if isinstance(mineral, int):
                    continue
                answer += fatigue[i][mineral]
            pick -= 1

    return answer