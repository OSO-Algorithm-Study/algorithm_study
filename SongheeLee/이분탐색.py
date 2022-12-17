'''
5 3
1
2
8
4
9
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))

houses.sort()
# 최소 간격
start = 1
# 최대 간격
end = (houses[-1] - houses[0]) / M

while(start <= end):
    mid = (start + end) // 2
    if target == nums[mid]:
        flag = 1
        break
    elif target > nums[mid]:
        start = mid + 1
    else:
        end = mid - 1
print(flag)