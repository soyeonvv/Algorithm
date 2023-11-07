from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * n)

answer = 0
while True:
    answer += 1
    # 1번
    belt.rotate(1)
    robot.rotate(1)
    robot[n - 1] = 0
    # 2번
    for i in range(n - 2, -1, -1):
        if robot[i] == 1 and robot[i + 1] != 1 and belt[i + 1] >= 1:
            robot[i], robot[i + 1] = 0, 1
            belt[i + 1] -= 1
    robot[n - 1] = 0
    # 3번
    if belt[0] != 0:
        robot[0] = 1
        belt[0] -= 1
    # 4번
    if belt.count(0) >= k:
        break

print(answer)