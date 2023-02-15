# 01 타일
import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * int(1e6+1) # dp = [0] * 1000001

dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 15746 

print(dp[n])

# 피보나치 수는 46번째 수가 2971215073가 되어 int의 범위를 초과하므로, 메모리초과가 난다.
# 따라서 모듈러 연산을 미리 해둔다.
# 규칙 : (i-2)번째 수들의 맨 앞(또는 뒤)에 00을 붙이고, (i-1)번째 수들의 맨 앞(또는 뒤)에 1을 붙이면 i번째 수들이 된다.
