import sys
input = sys.stdin.readline

dimen = [[([0] * 21) for _ in range(21)] for _ in range(21)]
# print(dimen)
# dimen[0][0][0] = 1

# print(dimen[0][0][0])

for i in range(21):
    for j in range(21):
        for k in range(21):
            # 경우 1의 경우
            if (i == 0) or (j == 0) or (k == 0):
                dimen[i][j][k] = 1
            elif (i < j) and (j < k):
                dimen[i][j][k] = dimen[i][j][k-1] + dimen[i][j-1][k-1] - dimen[i][j-1][k]
            else:
                dimen[i][j][k] = dimen[i-1][j][k] + dimen[i-1][j-1][k] + dimen[i-1][j][k-1] - dimen[i-1][j-1][k-1]

        
def find_result(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return dimen[20][20][20]
    elif a < b and b < c:
        return dimen[a][b][c-1] + dimen[a][b-1][c-1] - dimen[a][b-1][c]
    else:
        return dimen[a-1][b][c] + dimen[a-1][b-1][c] + dimen[a-1][b][c-1] - dimen[a-1][b-1][c-1]


while True:
    a, b, c = map(int, input().strip().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        result = find_result(a, b, c)
        print("w({0}, {1}, {2}) = ".format(a, b, c) + str(result))
    
    
        


    
