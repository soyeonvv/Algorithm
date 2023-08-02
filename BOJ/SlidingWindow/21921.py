import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visitors = list(map(int, input().split()))

start = sum(visitors[:x])
max_val = start
cnt = 1

for i in range(x, n):
    start = start - visitors[i - x] + visitors[i]
    if max_val < start:
        max_val = start
        cnt = 1
    elif max_val == start:
        cnt += 1
    else:
        continue
    
if max_val == 0:
    print('SAD')
else:
    print(max_val)
    print(cnt)