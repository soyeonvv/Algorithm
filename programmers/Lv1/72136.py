def solution(input_string):
    answer = []
    alpha = []

    alpha.append(input_string[0])
    for i in range(1, len(input_string)):
        if alpha[-1] == input_string[i]:
            continue
        if input_string[i] in alpha:
            answer.append(input_string[i])

        alpha.append(input_string[i])

    if not answer:
        return 'N'
    answer = list(set(answer))
    answer.sort()

    return ''.join(answer)