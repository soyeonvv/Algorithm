n = int(input())
a = [[0] * (n + 1)]
for _ in range(n):
    a.append([0] + list(map(int, input().split())))
total = sum(sum(i) for i in a)

def check(x, y, d1, d2):
    if x + d1 + d2 > n:
        return False
    if y - d1 < 1:
        return False
    if y + d2 > n:
        return False
    return True

def boundary(x, y, d1, d2):
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    graph[x][y] = 5
    for i in range(1, d1 + 1):
        graph[x + i][y - i] = 5
    for i in range(1, d2 + 1):
        graph[x + i][y + i] = 5
    for i in range(1, d2 + 1):
        graph[x + d1 + i][y - d1 + i] = 5
    for i in range(1, d1 + 1):
        graph[x + d2 + i][y + d2 - i] = 5
    return graph

def calculate_population(v1, v2, v3, v4, v5):
    cnt = 0
    for i in range(v1, v2):
        for j in range(v3, v4, v5):
            if graph[i][j] == 5:
                break
            cnt += a[i][j]
    return cnt

def calculate(x, y, d1, d2):
    people = [0] * 5

    # 1번 선거구 인구 계산
    people[0] = calculate_population(1, x + d1, 1, y + 1, 1)
    # 2번 선거구 인구 계산
    people[1] = calculate_population(1, x + d2 + 1, n, y, -1)
    # 3번 선거구 인구 계산
    people[2] = calculate_population(x + d1, n + 1, 1, y - d1 + d2, 1)
    # 4번 선거구 인구 계산
    people[3] = calculate_population(x + d2 + 1, n + 1, n, y - d1 + d2 - 1, -1)
    # 5번 선거구 인구 계산
    people[4] = total - sum(people)

    return max(people) - min(people)

answer = int(1e9)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for d1 in range(1, n + 1):
            for d2 in range(1, n + 1):
                if check(i, j, d1, d2):
                    # 5구역 경계 표시
                    graph = boundary(i, j, d1, d2)
                    answer = min(answer, calculate(i, j, d1, d2))

print(answer)