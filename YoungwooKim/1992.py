import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().strip())) for _ in range(N)]

def quad(x, y, N):
    for i in range(x, x + N):
        for j in range(y, y + N):
            if arr[i][j] != arr[x][y]:
                print("(", end="")
                quad(x, y, N//2)
                quad(x, y + N//2, N//2)
                quad(x + N//2, y, N//2)
                quad(x + N//2, y + N//2, N//2)
                print(")", end="")
                return

    if arr[x][y] == 1:
        print(1, end="")

    else :
        print(0, end="")

quad(0,0,N)