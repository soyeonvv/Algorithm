import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

maximum = int(-1e9)
minimum = int(1e9)

def calculate(operand1, operator, operand2):
    if operator == 0:
        return operand1 + operand2
    if operator == 1:
        return operand1 - operand2
    if operator == 2:
        return operand1 * operand2
    if operator == 3:
        return int(operand1 / operand2)
    
def dfs(k, value):
    if k == n - 1:
        global maximum, minimum
        maximum = max(maximum, value)
        minimum = min(minimum, value)
    else:
        global operators
        for i in range(4):
            if operators[i] >= 1:
                operators[i] -= 1
                dfs(k + 1, calculate(value, i, nums[k + 1]))
                operators[i] += 1

dfs(0, nums[0])
print(maximum)
print(minimum)