def solution(places):
    
    answer = []
    
    for place in places:
        problem = 0
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    problem = check_around(place, i, j)
                    
                if problem == 1:
                    answer.append(0)
                    break
            
            if problem == 1:
                break
                
        if i == 4 and j == 4 and problem == 0:
            answer.append(1)
    return answer


def check_around(place, i, j):
    problem = False
    
    print(place)
    
    # 좌, 우, 아래 체크 (+-1씩)
    if j-1 >= 0 and place[i][j-1] == "P":
        problem = True 
    elif j+1 <= 4 and place[i][j+1] == "P":
        problem = True 
    elif i+1 <= 4 and place[i+1][j] == "P":
        problem = True
    
    # 대각선(좌, 우) 체크 (+-1씩)
    if j-1>=0 and i+1<=4 and place[i+1][j-1]=="P" and (place[i+1][j] != "X" or place[i][j-1] != "X"):
        problem = True
    elif j+1<=4 and i+1<=4 and place[i+1][j+1]=="P" and (place[i+1][j] != "X" or place[i][j+1] != "X"):
        problem = True
        
    # 좌, 우, 아래 체크 (+-2씩)
    if j-2 >= 0 and place[i][j-2] == "P" and place[i][j-1] != "X":
        problem = True 
    elif j + 2 <= 4 and place[i][j+2] == "P" and place[i][j+1] != "X":
        problem = True 
    elif i+2 <= 4 and place[i+2][j] == "P" and place[i+1][j] != "X":
        problem = True
        
    return problem