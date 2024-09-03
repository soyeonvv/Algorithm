import heapq

def solution(program):
    answer = [0] * 10
    program.sort(key=lambda x: (x[1], x[0]))
    wait = []

    now = 0

    while program or wait:
        while program and program[0][1] <= now:
            heapq.heappush(wait, program.pop(0))

        if program and not wait:
            now = program[0][1]
            heapq.heappush(wait, program.pop(0))
        
        a, b, c = heapq.heappop(wait)

        answer[a - 1] += (now - b)
        now += c

    answer.insert(0, now)

    return answer