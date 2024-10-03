n = int(input())
a = list(map(int, input().split()))
a.sort()

cnt = 0
for i in range(n):
    temp = a[:i] + a[i + 1:]
    start, end = 0, len(temp) - 1

    while start < end:
        total = temp[start] + temp[end]
        if total == a[i]:
            cnt += 1
            break
        elif total < a[i]:
            start += 1
        else:
            end -= 1

print(cnt)