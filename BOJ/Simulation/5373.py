def rotate_90(graph):
    rotate_graph = list(map(list, zip(*graph[::-1])))
    return rotate_graph

def rotate_270(graph):
    rotate_graph = [x[::-1] for x in list(map(list, zip(*graph[::-1])))[::-1]]
    return rotate_graph

def cubing(side, d):
    global up, down, front, back, right, left
    if side == 'U':
        front_, back_, right_, left_ = [[0] * 3 for _ in range(4)]
        if d == '+':
            up = rotate_90(up)
            for i in range(3):
                front_[i], back_[i], right_[i], left_[i] = right[0][i], left[0][2 - i], back[0][2 - i], front[0][i]
        else:
            up = rotate_270(up)
            for i in range(3):
                front_[i], back_[i], right_[i], left_[i] = left[0][i], right[0][2 - i], front[0][i], back[0][2 - i]
        for i in range(3):
            front[0][i], back[0][i], right[0][i], left[0][i] = front_[i], back_[i], right_[i], left_[i]
    if side == 'D':
        front_, back_, right_, left_ = [[0] * 3 for _ in range(4)]
        if d == '+':
            down = rotate_90(down)
            for i in range(3):
                front_[i], back_[i], right_[i], left_[i] = left[2][i], right[2][2 - i], front[2][i], back[2][2 - i]
        else:
            down = rotate_270(down)
            for i in range(3):
                front_[i], back_[i], right_[i], left_[i] = right[2][i], left[2][2 - i], back[2][2 - i], front[2][i]
        for i in range(3):
            front[2][i], back[2][i], right[2][i], left[2][i] = front_[i], back_[i], right_[i], left_[i]
    if side == 'F':
        up_, down_, right_, left_ = [[0] * 3 for _ in range(4)]
        if d == '+':
            front = rotate_90(front)
            for i in range(3):
                up_[i], down_[i], right_[i], left_[i] = left[2 - i][2], right[2 - i][0], up[2][i], down[0][i]
        else:
            front = rotate_270(front)
            for i in range(3):
                up_[i], down_[i], right_[i], left_[i] = right[i][0], left[i][2], down[0][2 - i], up[2][2 - i]
        for i in range(3):
            up[2][i], down[0][i], right[i][0], left[i][2] = up_[i], down_[i], right_[i], left_[i]
    if side == 'B':
        up_, down_, right_, left_ = [[0] * 3 for _ in range(4)]
        if d == '+':
            back = rotate_270(back)
            for i in range(3):
                up_[i], down_[i], right_[i], left_[i] = right[i][2], left[i][0], down[2][2 - i], up[0][2 - i]
        else:
            back = rotate_90(back)
            for i in range(3):
                up_[i], down_[i], right_[i], left_[i] = left[2 - i][0], right[2 - i][2], up[0][i], down[2][i]
        for i in range(3):
            up[0][i], down[2][i], right[i][2], left[i][0] = up_[i], down_[i], right_[i], left_[i]
    if side == 'R':
        front_, back_, up_, down_ = [[0] * 3 for _ in range(4)]
        if d == '+':
            right = rotate_90(right)
            for i in range(3):
                front_[i], back_[i], up_[i], down_[i] = down[i][2], up[2 - i][2], front[i][2], back[2 - i][2]
        else:
            right = rotate_270(right)
            for i in range(3):
                front_[i], back_[i], up_[i], down_[i] = up[i][2], down[2 - i][2], back[2 - i][2], front[i][2]
        for i in range(3):
            front[i][2], back[i][2], up[i][2], down[i][2] = front_[i], back_[i], up_[i], down_[i]
    if side == 'L':
        front_, back_, up_, down_ = [[0] * 3 for _ in range(4)]
        if d == '+':
            left = rotate_90(left)
            for i in range(3):
                front_[i], back_[i], up_[i], down_[i] = up[i][0], down[2 - i][0], back[2 - i][0], front[i][0]
        else:
            left = rotate_270(left)
            for i in range(3):
                front_[i], back_[i], up_[i], down_[i] = down[i][0], up[2 - i][0], front[i][0], back[2 - i][0]
        for i in range(3):
            front[i][0], back[i][0], up[i][0], down[i][0] = front_[i], back_[i], up_[i], down_[i]

t = int(input())

for _ in range(t):
    up = [['w' for _ in range(3)] for _ in range(3)]
    down = [['y' for _ in range(3)] for _ in range(3)]
    front = [['r' for _ in range(3)] for _ in range(3)]
    back = [['o' for _ in range(3)] for _ in range(3)]
    left = [['g' for _ in range(3)] for _ in range(3)]
    right = [['b' for _ in range(3)] for _ in range(3)]

    cnt = int(input())
    commands = list(input().split())

    for side, d in commands:
        cubing(side, d)
    for i in range(3):
        print(up[i][0], up[i][1], up[i][2], sep='')