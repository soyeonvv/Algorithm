import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lecture = [list(map(int, input().split())) for _ in range(n)]
lecture = [x for x in lecture if x[0] != 5]
table = [[0] * 12 for _ in range(5)]
answer = 0

def isPossible(time):
    for i in range(time[1], time[2] + 1):
        if (table[time[0] - 1][i] == 1):
            return False
    return True

def select(time, check):
    for i in range(time[1], time[2] + 1):
        table[time[0] - 1][i] = check

def dfs(cnt, start):
    global k, answer
    if cnt == k:
        answer += 1
        return
    for i in range(start, len(lecture)):
        if (isPossible(lecture[i])):
            select(lecture[i], 1)
            dfs(cnt + (lecture[i][2] - lecture[i][1] + 1), i + 1)
            select(lecture[i], 0)

dfs(0, 0)
print(answer)