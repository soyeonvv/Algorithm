def check(x):
    stack = []
    
    for c in x:
        if c in ['(', '{', '[']:
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            elif c == ')' and stack[-1] == '(':
                stack.pop()
            elif c == '}' and stack[-1] == '{':
                stack.pop()
            elif c == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False

    return len(stack) == 0

def solution(s):
    answer = 0

    for i in range(len(s)):
        s = s[1:] + s[0]

        if check(s):
            answer += 1

    return answer