# https://www.acmicpc.net/problem/18310
# 안테나

import sys
input = sys.stdin.readline

N = int(input())
home = list(map(int, input().split()))

home.sort()

antenna = []

mid = (N-1) // 2

# 중간값 - 짝수일 때
if N % 2 == 0:
    for i in range(mid, mid+2):
        temp = 0
        for j in range(N):
            temp += abs(home[j] - home[i])
            antenna.append((temp, home[i]))
    antenna.sort()
    print(antenna[0][1])

# 중간값 - 홀수일 때
else:
    print(home[mid])


'''
4
5 1 7 9
'''