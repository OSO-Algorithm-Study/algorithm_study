def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    # print(citations)
    
    for idx in range(len(citations)):
        x = citations[idx]
        if x == idx+1:
            return idx + 1
        elif idx + 1 > x:
            return idx
    
    return len(citations)