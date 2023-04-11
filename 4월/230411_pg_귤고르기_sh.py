from collections import Counter

def solution(k, tangerine):
    
    counter = Counter(tangerine).most_common()
    print(counter)
    
    cnt = 0
    
    for temp in counter:
        if k <= 0:
            break
        cnt += 1
        temp_cnt = temp[1]
        k -= temp_cnt
    
    return cnt


