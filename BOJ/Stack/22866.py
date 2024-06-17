INF = int(1e9)

n = int(input())
buildings = list(map(int, input().split()))

cnt = [0] * n
near = [INF] * n

# 왼쪽 -> 오른쪽 탐색하면서 현재 빌딩의 높이보다 큰 빌딩 담는 스택
left = []

for i, height in enumerate(buildings):
    while left and buildings[left[-1]] <= height:
        left.pop()

    # 볼 수 있는 건물의 개수
    cnt[i] += len(left)

    # 가장 가까이에 있는 빌딩
    if left:
        if abs(i - left[-1]) < abs(near[i] - i):
            near[i] = left[-1]

    left.append(i)

# 오른쪽 -> 왼쪽 탐색하면서 현재 빌딩의 높이보다 큰 빌딩 담는 스택
right = []

for i in range(n - 1, -1, -1):
    height = buildings[i]
    
    while right and buildings[right[-1]] <= height:
        right.pop()
        
    cnt[i] += len(right)
    
    if right:
        if abs(i - right[-1]) < abs(near[i] - i):
            near[i] = right[-1]
    
    right.append(i)
    
for i in range(n):
    if cnt[i]:
        print(cnt[i], near[i] + 1)
    else:
        print(0)