t = int(input())
for _ in range(t):
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(n)]
    score.sort(key=lambda x:x[0])

    answer, prior = 1, score[0][1]
    for i in range(1, n):
        if score[i][1] < prior:
            prior = score[i][1]
            answer += 1

    print(answer)