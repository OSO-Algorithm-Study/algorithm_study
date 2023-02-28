def solution(board):
    global bingo
    
    O = []
    X = []
    dot = []
    
    idx = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
    bingo = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    
    # -------------
    # | 1 | 2 | 3 |
    # -------------
    # | 4 | 5 | 6 |
    # -------------
    # | 7 | 8 | 9 |
    # -------------
    
    for i in range(3):
        for j in range(3):
            mark = board[i][j]
            if mark == "O":
                O.append(idx.index((i, j)) + 1)
            elif mark == "X":
                X.append(idx.index((i, j)) + 1)
            else:
                dot.append(idx.index((i, j)) + 1)
    

    # 1. X의 개수 > O의 개수
    if len(X) > len(O):
        return 0
    
    # 2. O의 개수 - X의 개수 > 1
    if len(O) - len(X) > 1: 
        return 0
    
    # 3. O가 빙고일 때, X의 개수 >= O의 개수 (입출력 #2)
    if is_bingo(O) == 1:
        if len(X) >= len(O):
            return 0
    
    # 4. X가 빙고일 때, O가 많거나, X의 개수가 많을 때
    if is_bingo(X) == 1:
        if len(X) < len(O):
            return 0
        elif len(X) > len(O):
            return 0
    
    # 5. O와 X 모두 빙고일때
    if is_bingo(O) == 1 and is_bingo(X) == 1:
        return 0
    
    answer = 1
    
    return answer


def is_bingo(list_a):
    for b in bingo:
        counter = 0
        for temp in b:
            if temp in list_a:
                counter += 1
            # 빙고일 때 return 1
            if counter == 3:
                return 1
    
    return 0