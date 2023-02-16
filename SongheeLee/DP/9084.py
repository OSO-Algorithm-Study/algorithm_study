# 동전
import sys
input = sys.stdin.readline

N = int(input()) # 동전의 개수
coins = list(map(int, input().split())) # 동전의 종류
amount = int(input()) # 금액

dp = [0] * (amount+1)

for i in range(1, amount+1):
    for coin in coins:
        if i == coin:
            dp[i] = 1
        elif i > coin:
            dp[i] += dp[i-coin]

print(dp[amount])