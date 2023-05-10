import math
INF = int(1e9)

n, m = map(int, input().split())
pkg, single = INF, INF

for _ in range(m):
    p, s = map(int, input().split())
    pkg = min(pkg, p)
    single = min(single, s)

answer = 0

if pkg > single * 6:
    answer = single * n
elif pkg < (n % 6) * single:
    answer = pkg * math.ceil(n / 6)
else:
    answer = pkg * (n // 6) + single * (n % 6)

print(answer)