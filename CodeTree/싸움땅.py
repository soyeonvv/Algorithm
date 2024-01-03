n, m, k = map(int, input().split())
gun_graph = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    v = 0
    for j in list(map(int, input().split())):
        if j != 0:
            gun_graph[i][v].append(j)
        v += 1
player_graph = [[-1] * n for _ in range(n)]
player = []
points = [0] * m

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(m):
    x, y, d, s = map(int, input().split())
    player_graph[x - 1][y - 1] = i
    player.append([x - 1, y - 1, d, s, 0])

def get_gun(num, x, y, g):
    if gun_graph[x][y]:
        if max(gun_graph[x][y]) > g:
            player[num][4] = max(gun_graph[x][y])
            gun_graph[x][y].remove(max(gun_graph[x][y]))
            gun_graph[x][y].append(g)

def fight(p1, p2, x, y):
    compare = [[p1, player[p1][3], player[p1][4]], [p2, player[p2][3], player[p2][4]]]
    compare.sort(key=lambda x:(-(x[1] + x[2]), -x[1]))
    winner, loser = compare[0][0], compare[1][0]
    # winner 포인트 획득
    points[winner] += (compare[0][1] + compare[0][2]) - (compare[1][1] + compare[1][2])
    player[winner][0], player[winner][1] = x, y
    player_graph[x][y] = winner
    # loser 총 내려놓고 이동
    if player[loser][4] != 0:
        gun_graph[x][y].append(player[loser][4])
        player[loser][4] = 0
    nx, ny = x + dx[player[loser][2]], y + dy[player[loser][2]]
    if nx < 0 or nx >= n or ny < 0 or ny >= n or player_graph[nx][ny] != -1:
        for i in range(1, 5):
            d = (player[loser][2] + i) % 4
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and player_graph[nx][ny] == -1:
                player[loser][2] = d
                break
    player[loser][0], player[loser][1] = nx, ny
    player_graph[nx][ny] = loser
    get_gun(loser, nx, ny, player[loser][4])
    get_gun(winner, x, y, player[winner][4])

for _ in range(k):
    # 플레이어 이동
    num = 0
    for x, y, d, s, g in player:
        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            # 방향 전환
            d = (d + 2) % 4
            player[num][2] = d
            nx, ny = x + dx[d], y + dy[d]
        if player_graph[nx][ny] == -1:
            # 이동
            player_graph[x][y] = -1
            player_graph[nx][ny] = num
            player[num][0], player[num][1] = nx, ny
            # 총 획득
            if gun_graph[nx][ny]:
                get_gun(num, nx, ny, g)
        else:
            player_graph[x][y] = -1
            fight(num, player_graph[nx][ny], nx, ny)
        num += 1

print(*points)