# 연속합2
import sys
input = sys.stdin.readline

'''
10
10 -4 3 1 5 6 -35 12 21 -1
'''

n = int(input())
nums = [0] + list(map(int, input().split()))
newNums = []
dp = [0]*(n+1)

for i in range(n+1):
    if nums[i] >= 0:
        dp[i] =  dp[i-1] + nums[i]
    else:
        if dp[i-1] + nums[i] >= 0:
            dp[i] =  dp[i-1] + nums[i]
        else:
            newNums.append(dp[i-1])
        continue

twoNums = []
for i in range(1, len(newNums)):
    twoNums.append(newNums[i] + newNums[i-1])

print(newNums)
# print(max(twoNums))




'''
n = int(input())
nums = [0] + list(map(int, input().split()))
newNums = []
dp = [0]*(n+1)

for i in range(n+1):
    if nums[i] >= 0:
        dp[i] =  dp[i-1] + nums[i]
    else:
        if nums[i-1] >= 0:
            newNums.append(dp[i-1])
        continue

twoNums = []
for i in range(1, len(newNums)):
    twoNums.append(newNums[i] + newNums[i-1])

print(newNums)
print(max(twoNums))
'''