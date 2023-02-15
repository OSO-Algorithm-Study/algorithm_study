# 문제링크 https://school.programmers.co.kr/learn/courses/30/lessons/68936
# 프로그래머스 - 쿼드압축 후 개수세기

arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
result = [0, 0]

def solution(arr):
    global result
    
    S = len(arr[0]) # arr의 초기 길이


    def quad(x, y, length):
        start = arr[x][y]
        for i in range(x, x+length):
            for j in range(y, y+length):
                if arr[i][j] != start:
                    quad(x, y, length//2)
                    quad(x+length//2, y, length//2)
                    quad(x, y+length//2, length//2)
                    quad(x+length//2, y+length//2, length//2)
                    return 
        result[start] += 1
        
    quad(0, 0, S)
    
    return result

solution(arr)
print(result)
