def solution(n, m, section):
    answer = 0
    
    paint = [0] * n
    
    for s in section:
        paint[s-1] = 1
    
    for s in section:
        if paint[s-1] == 1:
            
            max_section = s + m - 1 if (s + m - 1 ) <= n else n
            
            for temp in range(s-1, max_section):
                if paint[temp] == 1:
                    paint[temp] = 0
            answer += 1
    
    
    return answer