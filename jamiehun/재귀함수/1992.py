# 요약 : 1780 종이의 개수 풀이와 유사함
# "(" ")" 를 잘 넣어줘야함
# return 값을 적절한 위치에 넣어줘야 통과 가능함

import sys
input = sys.stdin.readline

size = int(input())
tree = []

for i in range(size):
    tree.append(list(map(int, input().strip())))

output = str()    

# print(tree)


# 재귀함수 시작
# row, col = start idx

def quad_tree(row, col, size):
    global output
    
    intro = tree[row][col]
    
    # size가 1일때 탈출 조건 및 숫자 넣기
    if size == 1:
        output += str(intro)
        return
    
    
    for i in range(row, row + size):
        for j in range(col, col + size):
            if tree[i][j] == intro:
                continue
            elif tree[i][j] != intro:
                output += "("
                quad_tree(row, col, size//2)
                quad_tree(row, (col + size//2), size//2)
                quad_tree((row + size//2), col, size//2)
                quad_tree((row + size//2), (col + size//2), size//2)
                output += ")"
                return # 재귀가 전부 끝나고 나서는 return을 해야함
                
            # size가 1보다 큰데 한 섹션이 다 맞을 경우
        if i == (row + size-1) and j == (col + size-1):
            if intro == 0:         
                output += str("0")
            else:
                output += str("1")
            return  # ouput에 채운 다음에는 return 해야함
    return 
           
                    
quad_tree(0, 0, size)

print(output)