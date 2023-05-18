# DFS
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx + 1, result - numbers[idx])
            dfs(idx + 1, result + numbers[idx])
            
    dfs(0, 0)
        
    return answer

'''
# BFS
from collections import deque

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    queue = deque()
    queue.append((0, -1 * numbers[0]))
    queue.append((0, numbers[0]))
    
    while queue:
        idx, temp = queue.popleft()
        idx += 1
        if idx < n:
            queue.append((idx, temp - numbers[idx]))
            queue.append((idx, temp + numbers[idx]))
        else:
            if temp == target:
                answer += 1
        
    return answer 
'''

'''
# BruteForce
from itertools import product

def solution(numbers, target):
    answer = 0
    op = ['-', '+']
    result = list(product(op, repeat=len(numbers)))
    
    for i in result:
        sum = 0
        
        for j in range(len(numbers)):
            if i[j] == '-':
                sum -= numbers[j]
            else:
                sum += numbers[j]
                
        if sum == target:
            answer += 1
        
    return answer
'''