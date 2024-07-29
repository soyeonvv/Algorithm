import math

def solution(n, stations, w):
    answer = 0
    
    no_signal = []
    no_signal.append(stations[0] - w - 1)
    no_signal.append(n - (stations[-1] + w))
    for i in range(1, len(stations)):
        no_signal.append((stations[i] - w - 1) - (stations[i - 1] + w))
            
    for i in no_signal:
        answer += math.ceil(i / (w * 2 + 1))

    return answer