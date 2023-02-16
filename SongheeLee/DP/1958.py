import sys
input = sys.stdin.readline

S1 = list(input().strip())
S2 = list(input().strip())
S3 = list(input().strip())

len1 = len(S1)
len2 = len(S2)
len3 = len(S3)

dp = [[0]*(len2 + 1) for _ in range(len1+1)]

for i in range(1,len1 + 1) :
    for j in range(1,len2 + 1) :
        if S1[i-1] == S2[j-1] :
            dp[i][j] = dp[i-1][j-1] + 1
            S1andS2.append(S1[i-1])
        else :
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

len4 = len(S1andS2)
dp2 = [[0]*(len4 + 1) for _ in range(len3+1)]
for i in range(1,len3 + 1) :
    for j in range(1,len4 + 1) :
        if S3[i-1] == S1andS2[j-1] :
            dp2[i][j] = dp2[i-1][j-1] + 1
        else :
            dp2[i][j] = max(dp2[i-1][j],dp2[i][j-1])

print(dp2[len3][len4])