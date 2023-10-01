n, s = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0

def dfs(k, value):
    if k == n:
        global ans
        if value == s:
            ans += 1
    else:
        dfs(k + 1, value + nums[k])
        dfs(k + 1, value)

dfs(0, 0)
if s == 0:
    ans -= 1

print(ans)

'''
# 조합 사용
from itertools import combinations

n, s = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0

for i in range(1, n + 1):
    comb = combinations(nums, i)

    for x in comb:
        if sum(x) == s:
            ans += 1

print(ans)
'''