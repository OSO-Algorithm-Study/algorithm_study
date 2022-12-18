import sys
input = sys.stdin.readline

def cut_paper(r, c, N):
    global white_cnt, blue_cnt
    temp_cnt = 0
    
    for i in range(N):
        for j in range(N):
            temp_cnt += paper[r+i][c+j]     
    
    if temp_cnt == 0:
        white_cnt += 1

    elif temp_cnt == N*N:
        blue_cnt += 1

    else: 
        N = N//2
        cut_paper(r, c, N)
        cut_paper(r, c+N, N)
        cut_paper(r+N, c, N)
        cut_paper(r+N, c+N, N)


if __name__ == '_main_':
    N = int(input())
    paper = [list(map(int,input().split())) for _ in range(N)]

    white_cnt = 0
    blue_cnt = 0

    cut_paper(0, 0, N)

    print(white_cnt)
    print(blue_cnt)