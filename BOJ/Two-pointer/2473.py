n = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

v = 10 ** 10
answer = []
for i in range(n - 2):
    flag = 0
    start, end = i + 1, n - 1
    while start < end:
        mix = solutions[i] + solutions[start] + solutions[end]
        if abs(mix) < v:
            v = abs(mix)
            answer = [solutions[i], solutions[start], solutions[end]]

        if mix == 0:
            flag = 1
            break
        elif mix < 0:
            start += 1
        else:
            end -= 1

    if flag:
        break

print(* answer)