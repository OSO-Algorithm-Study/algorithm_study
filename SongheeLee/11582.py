import sys
input = sys.stdin.readline


N = int(input())
chickens = list(map(int, input().split()))
curr = int(input())
people = N

# chicken
def chicken_sort(start, end):
    # 가장 안쪽
    if (start + 1) == end:
        return

    # 반복
    chicken_sort(start, end//2)
    chickens[start : end//2].sort()
    chicken_sort(end//2, end)
    chickens[end//2 : end].sort()


    # 중간 단계 종결 조건

chicken_sort(0, people)
print(chickens) 


# # cutting paper
# def cuttingPaper(x, y, len):
#     global white_cnt, blue_cnt
#     temp = 0
    
#     for i in range(x, x+len):
#         for j in range(y, y+len):
#             temp += paper[i][j] 
    
#     if temp == 0:
#         white_cnt += 1
    
#     elif temp == len * len:
#         blue_cnt += 1
    
#     else:
#         len = len // 2
#         cuttingPaper(x, y, len)
#         cuttingPaper(x, y + len, len)
#         cuttingPaper(x + len, y, len)
#         cuttingPaper(x + len, y + len, len)

# N = int(input())

# paper = [list(map(int, input().split())) for _ in range(N)]

# blue_cnt = 0
# white_cnt = 0

# cuttingPaper(0, 0, N)

# print(white_cnt)
# print(blue_cnt)