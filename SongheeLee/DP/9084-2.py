# 동전
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input()) # 동전의 개수
    coins = list(map(int, input().split())) # 동전의 종류
    amount = int(input()) # 금액

    dp = [0] * (amount+1)
    dp[0] = 1 # 0개를 이용하여 0원을 만들 수 있다.

    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] += dp[i-coin]

    print(dp[amount])