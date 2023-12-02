graph = [list(map(int, input().split())) for _ in range(10)]
papers = [5] * 5
answer = int(1e9)

def dfs(x, y, cnt):
    global answer
    if y >= 10:
        answer = min(answer, cnt)
        return
    if x >= 10:
        dfs(0, y + 1, cnt)
        return
    
    if graph[x][y] == 1:
        for i in range(5):
            if papers[i] == 0:
                continue
            if x + i >= 10 or y + i >= 10:
                continue

            flag = 0
            for j in range(x, x + i + 1):
                for k in range(y, y + i + 1):
                    if graph[j][k] == 0:
                        flag = 1
                        break
                if flag:
                    break
            
            if flag == 0:
                for j in range(x, x + i + 1):
                    for k in range(y, y + i + 1):
                        graph[j][k] = 0
                papers[i] -= 1
                dfs(x + i + 1, y, cnt + 1)
                papers[i] += 1
                for j in range(x, x + i + 1):
                    for k in range(y, y + i + 1):
                        graph[j][k] = 1

    else:
        dfs(x + 1, y, cnt)

dfs(0, 0, 0)
if answer != int(1e9):
    print(answer)
else:
    print(-1)