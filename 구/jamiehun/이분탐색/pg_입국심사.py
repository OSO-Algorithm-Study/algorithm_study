def solution(n, times):
    answer = 0
    
    left, right = 1, max(times) * n 
    
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for time in times:
            people += (mid // time) # 심사관 1명당 mid분 동안 심사한 사람 수
            if people >= n:
                break
            
        if people >= n:
            answer = mid 
            right = mid - 1
        
        else:
            left = mid + 1
    
    return answer