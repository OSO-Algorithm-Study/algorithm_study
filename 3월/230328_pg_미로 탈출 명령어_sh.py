# 스택으로 풀기
# 큐로 풀면 시간복잡도 over
# 답안 참고 : https://comdoc.tistory.com/entry/%EB%AF%B8%EB%A1%9C-%ED%83%88%EC%B6%9C-%EB%AA%85%EB%A0%B9%EC%96%B4
from collections import deque

def solution(n, m, x, y, r, c, k):
    
    q = deque()
    q.append((x, y, []))
    result = 'impossible'
    
    while q:
        x_pos, y_pos, path = q.pop()
        
        if len(path) == k and (x_pos, y_pos) == (r, c):
            result = ''.join(path)
            break
        
        remain, shortest_path = k - len(path), abs(x_pos - r) + abs(y_pos - c)
        if remain < shortest_path or remain % 2 != shortest_path % 2:
            continue
        
        if x_pos > 1:
            q.append((x_pos - 1, y_pos, path + ['u']))
        if y_pos < m:
            q.append((x_pos, y_pos + 1, path + ['r']))
        if y_pos > 1:
            q.append((x_pos, y_pos - 1, path + ['l']))
        if x_pos < n:
            q.append((x_pos + 1, y_pos, path + ['d']))
    
    return result