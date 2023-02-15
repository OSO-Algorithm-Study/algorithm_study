# 문제링크 https://school.programmers.co.kr/learn/courses/30/lessons/68936
# 프로그래머스 - 쿼드압축 후 개수세기
result = [0, 0]

def solution(arr):
    global result
    
    S = len(arr[0]) # arr의 초기 길이

    
    start_number = arr[0][0]


    for i in range(S):
        for j in range(S):
            if arr[i][j] != start_number:
                break
            elif arr[i][j] == start_number:
                continue
            elif arr[i][j] == start_number and i == (S-1) and j == (S-1):
                if start_number == 0:
                    result[0] += 1
                else:
                    result[1] += 1
                return result
        if arr[i][j] != start_number:
            break



    quad(0, 0, S//2, arr)
    quad(0, 0 + S//2, S//2, arr)
    quad(0 + S//2, 0, S//2, arr)
    quad(S//2, S//2, S//2, arr)

    return result  

def quad(x, y, length, arr):
    global result
    start_number = arr[x][y]
    
    if length == 1:
        if start_number == 0:
            result[0] += 1
        else:
            result[1] += 1
        return
    
    
    for i in range(x, x + length):
        for j in range(y, y + length):
            if start_number == arr[i][j] and i == (x + length - 1) and j == (y + length - 1):
                if start_number == 0:
                    result[0] += 1
                else:
                    result[1] += 1
                return
            
            elif start_number == arr[i][j]:
                continue
            
            else:
                quad(x, y, length//2, arr)
                quad(x, y + length//2, length//2, arr)
                quad(x + length//2, y, length//2, arr)
                quad(x + length//2, y + length//2, length//2, arr)
                return
                