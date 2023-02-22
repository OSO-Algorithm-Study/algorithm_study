# 주의 : union_parent에서 최소값으로 하는 것이 만능은 아니다! (마지막에 체크해줘야할 때도 있음)
# 반례참고 https://school.programmers.co.kr/questions/40414

def solution(n, computers):
    global parent
    # 인덱스 잘 확인하기
    parent = list()
    for i in range(n):
        parent.append(i)
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            
            if computers[i][j]:
                parent_i = parent[i]
                parent_j = parent[j]
                
                if parent_i != parent_j:
                    union_parent(i, j, parent)
    
    result = set()
    for temp in parent:
        temp = find_parent(temp, parent) # 다시 한번 parent 값 참고 필수! (무조건 union_parent를 최소값으로 한다고 답이 아님)
        result.add(temp)
    
    return len(result)

    
def find_parent(a, parent):
    if parent[a] != a:
        parent[a] = find_parent(parent[a], parent)
    return parent[a]    
    
    
def union_parent(i, j, parent):
    a = find_parent(i, parent)
    b = find_parent(j, parent)
    
    if a < b :
        parent[b] = a
    elif a > b:
        parent[a] = b
        
n = 7
computers = [[1, 0, 0, 0, 0, 0, 1], [0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0], [0, 0, 0, 0, 1, 1, 1], [1, 0, 0, 0, 0, 1, 1]]

result = solution(7, computers)
print(result)