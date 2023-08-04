array = [int(input()) for _ in range(10)]

score = 0

for i in array:
    score += i
    if score == 100:
        break
    elif score > 100:
        if score - 100 <= 100 - (score - i):
            break
        else:
            score -= i
            break

print(score)