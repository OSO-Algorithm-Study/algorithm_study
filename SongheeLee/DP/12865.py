# 아주 평범한 배낭
'''
4 7
6 13
4 8
3 6
5 12
'''
import sys
input = sys.stdin.readline

N, weightLimit = map(int, input().split())
maxValue = 0
objects = []

for _ in range(N):
    weight, value = map(int, input().split())
    objects.append((weight, value))

dp = [0] * (weightLimit+1)

for i in range(1, weightLimit+1):
    for weight, value in objects:
        if weight <= i:
            if dp[i] < dp[i-weight] + value:
                dp[i] = dp[i-weight] + value
            if maxValue < dp[i]:
                maxValue = dp[i]


print(dp)
print(maxValue)