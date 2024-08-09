from collections import defaultdict

n, d, k, c = map(int, input().split())
dishes = [int(input()) for _ in range(n)]
# 회전 초밥 고려
dishes = dishes + dishes[:k - 1]

dic = defaultdict(int)
dic[c] += 1
answer, start = 0, 0

for i in range(n + k):
    if i == n + k - 1:
        answer = max(answer, len(dic))
        continue
    if i >= k:
        answer = max(answer, len(dic))
        dic[dishes[start]] -= 1
        if dic[dishes[start]] == 0:
            dic.pop(dishes[start])
        start += 1

    dic[dishes[i]] += 1

print(answer)