from collections import defaultdict

g, s = map(int, input().split())
w = list(input())
str = list(input())

dic1 = defaultdict(int)
for i in w:
    dic1[i] += 1
dic2 = defaultdict(int)

answer, start, cnt = 0, 0, 1
for i in str:
    dic2[i] += 1
    if cnt == g:
        if dic1 == dic2:
            answer += 1
        dic2[str[start]] -= 1
        if dic2[str[start]] == 0:
            dic2.pop(str[start])
        start += 1
        cnt -= 1
    cnt += 1

print(answer)