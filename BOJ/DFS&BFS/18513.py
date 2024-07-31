from collections import deque

n, k = map(int, input().split())
fountain = list(map(int, input().split()))

queue = deque()
dic = {}

for i in fountain:
    dic[i] = 0
    queue.append(i)

house, answer = 0, 0

def build(pos, x):
    global house, answer
    if x not in dic.keys():
        dic[x] = dic[pos] + 1
        house += 1
        answer += dic[x]
        if house == k:
            return -1
        else:
            queue.append(x)

while queue:
    pos = queue.popleft()
    l, r = pos - 1, pos + 1
    if build(pos, l) == -1:
        break
    if build(pos, r) == -1:
        break

print(answer)