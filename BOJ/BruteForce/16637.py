n = int(input())
formula = list(input())
for i in range(0, len(formula), 2):
    formula[i] = int(formula[i])
answer = -int(1e9)

def calculate(num1, num2, s):
    if s == '+':
        return num1 + num2
    elif s == '-':
        return num1 - num2
    elif s == '*':
        return num1 * num2

def dfs(i, value):
    global answer
    if i == n:
        answer = max(answer, value)
        return
    if i + 3 < n:
        dfs(i + 4, calculate(value, calculate(formula[i + 1], formula[i + 3], formula[i + 2]), formula[i]))
    dfs(i + 2, calculate(value, formula[i + 1], formula[i]))

if n == 1:
    answer = formula[0]
else:
    dfs(1, formula[0])
print(answer)