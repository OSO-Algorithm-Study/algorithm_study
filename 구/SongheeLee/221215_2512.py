# 예산
# 이분탐색
# 문제링크 https://www.acmicpc.net/problem/2512

import sys
input = sys.stdin.readline

N = int(input());
budgets = list(map(int, input().split()))
total_budget = int(input())

sum = 0
budgets.sort()

start = 0
end = budgets[N-1]


while start <= end:
    mid = (start + end) // 2
    sum = 0
    for budget in budgets:
        if budget <= mid:
            sum += budget
        else:
            sum += mid
    
    if (sum <= total_budget):
        start = mid + 1
    else:
        end = mid - 1
        
print(mid)