def search(b, start, end, target):
    result = start
    while start <= end:
        mid = (start + end) // 2
        if b[mid] < target:
            result = mid + 1
            start = mid + 1
        else:
            end = mid - 1
    return result

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b.sort()

    answer = 0

    for i in range(n):
        answer += search(b, 0, m - 1, a[i])
    
    print(answer)