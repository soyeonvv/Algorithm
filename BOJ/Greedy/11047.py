n, k = map(int, input().split())
a_list = []
for _ in range(n):
    a_list.append(int(input()))
a_list.sort(reverse=True)
cnt = 0
for a in a_list:
    if k == 0:
        break
    cnt += (k // a)
    k %= a  
print(cnt)