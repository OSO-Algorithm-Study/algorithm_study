import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

zero_cnt = 0
one_cnt = 0

def quad(N, x, y):

    global zero_cnt, one_cnt
    
    for i in range(x, x + N):
        for j in range(y, y + N):
            
            if arr[x][y] != arr[i][j]:
                quad(N//2, x, y)
                quad(N//2, x + N//2, y)
                quad(N//2, x, y + N//2)
                quad(N//2, x + N//2, y + N//2)
                return

    if arr[x][y] == 0:
        zero_cnt += 1
    else :
        one_cnt += 1

quad(n, 0, 0)
print([zero_cnt, one_cnt])