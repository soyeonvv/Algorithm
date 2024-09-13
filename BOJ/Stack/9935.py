str = input()
bomb = list(input())
n = len(bomb)

stack = []

for s in str:
    stack.append(s)
    if stack[-n:] == bomb:
        for i in range(n):
            stack.pop()

if not stack:
    print('FRULA')
else:
    print(''.join(stack))