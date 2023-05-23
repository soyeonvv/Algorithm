from math import ceil

def to_minutes(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

def solution(fees, records):
    answer = []
    cars = {}

    for record in records:
        time, car, info = record.split()

        if car in cars:
            cars[car].append([time, info])
        else:
            cars[car] = [[time, info]]

        cars = dict(sorted(cars.items()))

    for car in cars:
        total = 0
        pay = fees[1]

        if len(cars[car]) % 2 != 0:
            cars[car].append(["23:59", "OUT"])

        for i in cars[car]:
            if i[1] == 'IN':
                total -= to_minutes(i[0])
            else:
                total += to_minutes(i[0])

        if total > fees[0]:
            pay += ceil((total - fees[0]) / fees[2]) * fees[3]
        
        answer.append(pay)

    return answer