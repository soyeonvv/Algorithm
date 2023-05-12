def minute(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

def solution(book_time):
    answer = 0
    rooms = [0 for _ in range(24 * 60 + 10)]

    for i in book_time:
        check_in = minute(i[0])
        check_out = minute(i[1]) + 10

        rooms[check_in] += 1
        rooms[check_out] -= 1

    for i in range(1, len(rooms)):
        rooms[i] += rooms[i - 1]

    answer = max(rooms)

    return answer