# 쿼드압축 후 개수 세기
# 분할정복
# https://school.programmers.co.kr/learn/courses/30/lessons/68936
'''
· 종이 자르기와 같은 문제
· global 변수 쓰는 법
· 이차원 배열에서 len
'''

num0 = 0
num1 = 0

def solution(arr):
    
    global num0, num1
    
    N = len(arr[0])
        
    quad(arr, 0, 0, N)
        
    answer = N
    
    answer = []
    answer.append(num0)
    answer.append(num1)
        
    return answer

def quad(arr, r, c, N):

    global num0, num1
    
    temp = 0
    
    for i in range(N):
        for j in range(N):
            temp += arr[r+i][c+j]
    
    if (temp == 0):
        num0 += 1
        
    elif (temp == N*N):
        num1 += 1
    
    else:
        quad(arr, r, c, N//2)
        quad(arr, r + N//2, c, N//2)
        quad(arr, r, c + N//2, N//2)
        quad(arr, r + N//2, c + N//2, N//2)
    
