from collections import Counter

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

def calculate():
    max_len = 0
    for i in range(len(A)):
        a = [x for x in A[i] if x != 0]
        counter = Counter(a)
        counter = sorted(counter.items(), key=lambda x:(x[1], x[0]))
        A[i] = []
        for key, value in counter:
            A[i].append(key)
            A[i].append(value)

        if max_len  < len(A[i]):
            max_len = len(A[i])

    for i in range(len(A)):
        for _ in range(max_len - len(A[i])):
            A[i].append(0)
        A[i] = A[i][:100]

for time in range(101):
    try:
        if A[r - 1][c - 1] == k:
            print(time)
            break
    except:
        pass

    if len(A) >= len(A[0]):
        calculate()
    else:
        A = list(zip(*A))
        calculate()
        A = list(zip(*A))
else:
    print(-1)