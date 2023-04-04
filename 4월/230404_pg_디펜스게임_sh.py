# https://school.programmers.co.kr/questions/40999
# 답안참고

import heapq

def solution(n, k, enemy):
    answer = 0
    heap_list = []
    
    for e in enemy:
        heapq.heappush(heap_list, -e)
        
        if n >= e:
            n -= e
            answer += 1
        
        else:
            if k:
                n += (-heapq.heappop(heap_list) - e)
                k -= 1
                answer += 1
            else:
                break 
        
    return answer
                
    
    
    
    

# n = 7
# k = 3
# enemy = [4, 2, 4, 5, 3, 3, 1]

# n = 2
# k = 4
# enemy = [3, 3, 3, 3]

n = 3
k = 5
enemy = [3, 3, 3, 3]

result = solution(n, k , enemy)
print(result)