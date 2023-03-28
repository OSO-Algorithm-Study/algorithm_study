# 풀다가 포기.. 
# 채점 결과
# 정확성: 36.4
# 합계: 36.4 / 100.0

def solution(commands):
    global table
    global merge_table
    answer = []
    table = [([0] * 51) for _ in range(51)]
    merge_table = [([0] * 51) for _ in range(51)]

    for command in commands:
        statement = list(map(str, command.split()))
        
        statement_length = len(statement)
        
        if statement[0] == "UPDATE":
            # UPDATE CASE1
            if statement_length == 4:
                update_case1(int(statement[1]), int(statement[2]), statement[3])
            
            # UPDATE CASE2
            else: 
                update_case2(statement[1], statement[2])
                
            
        elif statement[0] == "MERGE":
            merge_case(int(statement[1]), int(statement[2]), int(statement[3]), int(statement[4]))
        
        elif statement[0] == "UNMERGE":
            unmerge_case(int(statement[1]), int(statement[2]))
            # print('WHEN2', merge_table[1][4])
        
        else:
            result = print_case(int(statement[1]), int(statement[2]))
            answer.append(result)           

    return answer
    

def update_case1(r, c, value):
    table[r][c] = value
    
    if merge_table[r][c] == 0:
        return
    else:
        for temp in merge_table[r][c]:
            table[temp[0]][temp[1]] = value
    
    return
    

def update_case2(value1, value2):
    for i in range(51):
        for j in range(51):
            if table[i][j] == value1:
                table[i][j] = value2
                
                
def merge_case(r1, c1, r2, c2):
    if r1 == r2 and c1 == c2:
        return
    
    if table[r1][c1] == 0 and table[r2][c2] != 0:
        table[r1][c1] = table[r2][c2]
        
    
    elif table[r1][c1] != 0 and table[r2][c2] == 0:
        table[r2][c2] = table[r1][c1]
        
    elif table[r1][c1] != 0 and table[r2][c2] != 0:
        table[r2][c2] = table[r1][c1]
        
    add_to_merge_table(r1, c1, r2, c2)
  
    return

def add_to_merge_table(r1, c1, r2, c2):
    if merge_table[r1][c1] == 0:
        merge_table[r1][c1] = set()
        merge_table[r1][c1].add((r2, c2))
    else:
        merge_table[r1][c1].add((r2,c2))
    
    if merge_table[r2][c2] == 0:
        merge_table[r2][c2] = set()
        merge_table[r2][c2].add((r1, c1))
    else:
        merge_table[r2][c2].add((r1,c1))
    
    mix = merge_table[r1][c1].union(merge_table[r2][c2])
    
    merge_table[r1][c1] = mix
    merge_table[r2][c2] = mix
    
    return
        

def unmerge_case(r, c):
    value = table[r][c]
    
    for temp in merge_table[r][c]:
        if temp[0] == r and temp[1] == c:
            continue
        else:
            merge_table[temp[0]][temp[1]] = 0
            table[temp[0]][temp[1]] = 0
        
    merge_table[r][c] = 0
    
    table[r][c] = value
    return

def print_case(r, c):
    if table[r][c] != 0:
        return table[r][c]
    else:
        return "EMPTY"
            


