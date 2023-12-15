n, m, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
enemy = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            enemy.append([i, j])
graph.append([0] * m)
answer = 0

def process():
    enemy_copy = [x[:] for x in enemy]
    result = 0

    while True:
        if len(enemy_copy) == 0:
            return result
        # 궁수 공격
        attack = set()
        for i in range(m):
            if graph[n][i] == 1:
                candidates = []
                e = 0
                for ex, ey in enemy_copy:
                    distance = abs(n - ex) + abs(i - ey)
                    if distance <= d:
                        candidates.append((distance, ey, e))
                    e += 1
                if candidates:
                    candidates.sort(key=lambda x:(x[0], x[1]))
                    attack.add(candidates[0][2])
        # 공격 받은 적 게임에서 제외
        a = sorted(attack, reverse=True)
        for i in a:
            del enemy_copy[i]
            result += 1
        # 적 아래로 한칸 이동
        remove = []
        for i in range(len(enemy_copy)):
            enemy_copy[i][0] += 1
            if enemy_copy[i][0] == n:
                remove.append(i)
        remove.sort(reverse=True)
        for i in remove:
            del enemy_copy[i]

def dfs(start, cnt):
    global answer
    if cnt == 3:
        answer = max(answer, process())
        return
    for i in range(start, m):
        graph[n][i] = 1
        dfs(i + 1, cnt + 1)
        graph[n][i] = 0

# 궁수 3명 배치
dfs(0, 0)

print(answer)