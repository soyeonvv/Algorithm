array = []
for _ in range(9):
    array.append(int(input()))

array.sort()
x = sum(array) - 100

for i in range(0, 8):
    for j in range(i + 1, 9):
        if array[j] == x - array[i]:
            one = array[i]
            two = array[j]

array.remove(one)
array.remove(two)
array.sort()

for i in array:
    print(i)