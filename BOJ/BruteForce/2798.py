from itertools import permutations

n, m = map(int, input().split())

card = list(map(int, input().split()))

array = permutations(card, 3)
answer = 0

for i in array:
    if(m >= sum(i)):
        answer = max(answer, sum(i))

print(answer)