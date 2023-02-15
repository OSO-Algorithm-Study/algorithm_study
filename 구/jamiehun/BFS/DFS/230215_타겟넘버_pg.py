from collections import deque

def solution(numbers, target):
    result = bfs(numbers, target)
    print(result)
    
    return result
    
def bfs(numbers, target):
    result = 0
    idx = 0
    size = len(numbers)
    temp = numbers[idx]
    q = deque([])
    q.append((idx, temp))
    q.append((idx, -temp))
    
    while q:
        comb = q.popleft()
        idx = comb[0]
        number = comb[1]
        
        if number == target:
            result += 1
        
        if idx == (size-1):
            continue
        
        temp = numbers[idx+1]
        
        q.append((idx+1, number+temp))
        q.append((idx+1, number-temp))
        
    return result

numbers = [1, 1, 1, 1, 1]
target = 3

r = solution(numbers, target)
print(r)
        