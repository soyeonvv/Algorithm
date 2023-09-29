t = int(input())

for i in range(t):
    students = list(map(int, input().split()))
    answer = 0
    for j in range(1, len(students)):
        for k in range(1, j):
            if students[k] > students[j]:
                answer += 1

    print(i + 1, answer)