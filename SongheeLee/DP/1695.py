'''
5
1 2 3 4 2
'''
# 팰린드롬 만들기

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
length = len(nums)//2 + 1
dp = [[0]*length]*length

# 다르면 오른쪽, 하나 행 추가
# 같으면 대각선
# 끝날때까지

rowNums = [0]
colNums = [0]
for i in range(0, len(nums)//2):
    rowNums.append(nums[i])

for i in range(len(nums)-1, len(nums)//2, -1):
    colNums.append(nums[i])

i = 1;
j = 1;
while(i<len(rowNums)):
   
    if(rowNums[i] == colNums[j]):
        dp[j][i] = max(dp[j-1][i-1], dp[j][i-1])
        i += 1
        j += 1
    else:
        dp[j][i] =  1
        i += 1
        rowNums.append(nums[len(rowNums)])

print(dp)
