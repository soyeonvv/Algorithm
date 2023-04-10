k, n = map(int, input().split())
array = []

for _ in range(k):
    array.append(int(input()))

start = 1
end = max(array)

while(start <= end):
    num = 0
    mid = (start + end) // 2
    
    for x in array:
        num += x // mid
    if num >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)