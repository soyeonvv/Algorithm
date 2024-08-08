from collections import defaultdict

n, k = map(int, input().split())
students = [len(input()) for _ in range(n)]

dic = defaultdict(int)
answer, start = 0, 0
for i in range(n):
    if i > k:
        dic[students[start]] -= 1
        start += 1

    answer += dic[students[i]]
    dic[students[i]] += 1

print(answer)