def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x: (x[col-1], -x[0]))
    
    S_i = []
    
    for i in range(row_begin-1, row_end):
        total = 0
        for j in data[i]:
            total += (j % (i+1))
        S_i.append(total)
    
    # print(S_i)
    answer = S_i[0]
    
    for s in range(1, len(S_i)):
        s2 = S_i[s]
        answer = answer ^ s2
    
    return answer