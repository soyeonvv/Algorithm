def solution(s):
    answer = -1
    stack = []

    for c in s:
        if len(stack) == 0:
            stack.append(c)
        else:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)

    if len(stack) == 0:
        answer = 1
    else:
        answer = 0

    return answer