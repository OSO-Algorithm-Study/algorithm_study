import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

maximum = 21

dp = [[[0] * maximum for _ in range(maximum)] for _ in range(maximum)]

def w(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)    # index error

    if dp[a][b][c]:
        return dp[a][b][c]

    if a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]

    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]

while True:

    a, b, c = map(int, input().split())
        
    if a == -1 and b == -1 and c == -1:
        break

    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')