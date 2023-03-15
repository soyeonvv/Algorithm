f = input().split('-')
result = 0

for i in f[0].split('+'):
    result += int(i)
for i in f[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)