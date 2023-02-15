import sys
input = sys.stdin.readline

'''
ACAYKP
CAPCAK
'''

row = input().strip()
col = input().strip()

dp = [[0] * len(row)] * len(col)
lenLCS = 0

for i in range(len(row)):
    for j in range(len(col)):
        if col[j] == row[i]:
            if i>=1 and j>=1:
                dp[j][i] = dp[j-1][i-1] + 1
            else:
                dp[j][i] = 1
            
            if dp[j][i] > lenLCS:

        if dp[j][i] > 0:
            prev = lenLCS
                lenLCS = dp[j][i] 

print(lenLCS)
