n, m, l = map(int, input().split())
stations = [0] + list(map(int, input().split())) + [l]
stations.sort()

start, end = 1, l - 1
answer = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(1, len(stations)):
        if stations[i] - stations[i - 1] > mid:
            cnt += (stations[i] - stations[i - 1] - 1) // mid
    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid

print(answer)