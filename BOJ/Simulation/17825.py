dice = list(map(int, input().split()))

graph = [[i for i in range(0, 41, 2)],
         [10, 13, 16, 19, 25, 30, 35, 40],
         [20, 22, 24, 25, 30, 35, 40],
         [30, 28, 27, 26, 25, 30, 35, 40]]

def dfs(depth, score, horses):
    global answer
    if depth == 10:
        answer = max(answer, score)
        return

    for i in range(4):
        if horses[i][0] != -1:
            temp = [row[:] for row in horses]
            temp[i][0] += dice[depth]

            # 파란색 칸
            if temp[i][1] == 0:
                if temp[i][0] == 5:
                    temp[i][1] = 1
                    temp[i][0] = 0
                elif temp[i][0] == 10:
                    temp[i][1] = 2
                    temp[i][0] = 0
                elif temp[i][0] == 15:
                    temp[i][1] = 3
                    temp[i][0] = 0

            if temp[i][0] >= len(graph[temp[i][1]]): # 도착
                temp[i][0] = -1
                dfs(depth + 1, score, temp)
            else:
                flag = False
                s = graph[temp[i][1]][temp[i][0]]
                for j in range(4):
                    if temp[j][0] == -1:
                        continue
                    if j != i and graph[temp[j][1]][temp[j][0]] == s:
                        if s == 30:
                            if (temp[i] == [0, 3] and temp[j] == [0, 3]) or (temp[i] != [0, 3] and temp[j] != [0, 3]):
                                flag = True
                                break
                        elif s in [16, 22, 24, 26, 28]:
                            if temp[i] == temp[j]:
                                flag = True
                                break
                        else:
                            flag = True
                            break
                if flag:
                    continue
                dfs(depth + 1, score + graph[temp[i][1]][temp[i][0]], temp)

answer = 0
horses = [[0, 0]] * 4
dfs(0, 0, horses)
print(answer)