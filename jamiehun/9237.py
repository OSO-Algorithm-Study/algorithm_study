# https://www.acmicpc.net/problem/9237
# 9327번 : 이장님 초대

import sys
input = sys.stdin.readline 

n = int(input())
grow = list(map(int, input().split()))
grow.sort(reverse = True)

day_count = []
for i in range(n):
    day_count.append(i + 1)
# print(day_count)

for i in range(n):
    day_count[i] += grow[i] + 1

print(max(day_count))