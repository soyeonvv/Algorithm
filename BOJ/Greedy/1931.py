import sys

N = int(sys.stdin.readline())
time_list = []
for _ in range(N):
    time_list.append(list(map(int, sys.stdin.readline().split())))

time_list.sort(key=lambda x:(x[1], x[0]))
end_time = 0
cnt = 0
for start, end in time_list:
    if start >= end_time:
        cnt += 1
        end_time = end
print(cnt)