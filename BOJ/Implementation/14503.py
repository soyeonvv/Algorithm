n, m = map(int, input().split())
r, c, d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

visited[r][c] = 1
cnt = 1

# 북 동 하 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    flag = 0

    for _ in range(4):
        # 왼쪽으로 90도 회전
        d = (d + 3) % 4
        nx, ny = r + dx[d], c + dy[d]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                r, c = nx, ny
                flag = 1
                break
    
    if flag == 0:
        if graph[r - dx[d]][c - dy[d]] == 1:
            print(cnt)
            break
        else:
            r, c = r - dx[d], c - dy[d]