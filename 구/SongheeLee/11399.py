# 5
# 3 1 4 3 2

import sys
input = sys.stdin.readline

N = int(input())
waiting = list(map(int, input().split()))

waiting.sort()

def fibo(i):
    if i == 0:
        return waiting[0]
    
    return waiting[i] + fibo(i-1)

sum = 0

for i in range(N):
    sum += fibo(i)

print (sum)
# print(fibo(N-1))