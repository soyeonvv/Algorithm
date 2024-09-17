n, k = map(int, input().split())
num = list(map(int, input()))

stack = []
for i in num:
    while stack:
        if stack[-1] < i and k > 0:
            stack.pop()
            k -= 1
        else:
            break
    stack.append(i)

while k > 0:
    stack.pop()
    k -= 1

answer = ''.join(map(str, stack))
print(int(answer))