n = int(input())
towers = list(map(int, input().split()))

stack, answer = [(towers[0], 1)], [0]

for i in range(1, n):
    while True:
        if not stack:
            answer.append(0)
            stack.append((towers[i], i + 1))
            break
        if stack[-1][0] < towers[i]:
            stack.pop()
        else:
            answer.append(stack[-1][1])
            stack.append((towers[i], i + 1))
            break

print(' '.join(map(str, answer)))