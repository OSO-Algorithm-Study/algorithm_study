# https://www.acmicpc.net/problem/1449
# 1449번: 수리공 항승

import sys
input = sys.stdin.readline

# n은 새는 곳의 개수, l은 테이프의 길이
n, l = map(int, input().split())
pipes = list(map(int, input().split()))

# print(tapes)
pipes.sort()

coverage = []

coverage.append(pipes[0] - 0.5)
coverage.append(coverage[0] + l)
count = 1

for i in range(1, n):
    if coverage[0] < pipes[i] < coverage[1]:
        continue
    else:
        coverage[0] = pipes[i] - 0.5
        coverage[1] = coverage[0] + l 
        count += 1

print(count)
 

# for i in tapes:
#     min_num = (i - l) - 0.5 if (i - l) > 0 else 0
#     max_num = (i + l) + 0.5 
#     coverage.append((min_num, max_num))
    
# print(coverage)
# count = 0
# for i in range(len(coverage)):
#     if i == 0:
#         min_cover = coverage[i][0]
#         max_cover = coverage[i][1]
#         count += 1
#     elif coverage[i][0] <= min_cover and max_cover <= coverage[i][1]:
#         continue
#     else:
#         min_cover = coverage[i][0]
#         max_cover = coverage[i][1]
#         count += 1

# print(count)
    