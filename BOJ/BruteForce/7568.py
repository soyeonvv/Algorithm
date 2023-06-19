n = int(input())

people = []

for _ in range(n):
    w, h = map(int, input().split())
    people.append((w, h))

for i in people:
    rank = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')