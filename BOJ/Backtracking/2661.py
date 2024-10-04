n = int(input())

def check(num):
    for i in range(n):
        temp = num[i:]
        for j in range(1, len(temp) // 2 + 1):
            check = temp[:j]
            if check == temp[j:j + j]:
                return False
    return True

def dfs(num):
    if not check(num):
        return -1

    if len(num) == n:
        print(''.join(map(str, num)))
        return 0

    for i in range(1, 4):
        num.append(i)
        if dfs(num) == 0:
            return 0
        num.pop()

dfs([])