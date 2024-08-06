def solution(rows, columns, queries):
    answer = []
    graph = [[0] * columns]
    for i in range(rows):
        row = [0]
        for j in range(i * columns + 1, (i + 1) * columns + 1):
            row.append(j)
        graph.append(row)

    def get_arr():
        rotate = []
        
        for i in range(y1, y2 + 1):
            rotate.append(graph[x1][i])
            graph[x1][i] = 0
        for i in range(x1 + 1, x2 + 1):
            rotate.append(graph[i][y2])
            graph[i][y2] = 0
        for i in range(y2 - 1, y1 - 1, -1):
            rotate.append(graph[x2][i])
            graph[x2][i] = 0
        for i in range(x2 - 1, x1, -1):
            rotate.append(graph[i][y1])
            graph[i][y1] = 0
        
        return rotate
    
    def fill():
        for i in range(y1, y2 + 1):
            graph[x1][i] = rotate.pop(0)
        for i in range(x1 + 1, x2 + 1):
            graph[i][y2] = rotate.pop(0)
        for i in range(y2 - 1, y1 - 1, -1):
            graph[x2][i] = rotate.pop(0)
        for i in range(x2 - 1, x1, -1):
            graph[i][y1] = rotate.pop(0)
    
    for x1, y1, x2, y2 in queries:
        rotate = get_arr()
        
        answer.append(min(rotate))
        rotate = [rotate.pop()] + rotate
        
        fill()

    return answer