# 4
# 120 110 140 150
# 485

import sys
input = sys.stdin.readline

N = int(input());
budgets = list(map(int, input().split()))
total_budget = int(input())

sum = 0
budgets.sort()

start = budgets[0]
end = budgets[N-1]


for i in range(N):
    sum += budgets[i]

if sum <= total_budget:
    print(budgets[N-1])

else:
    if min(budgets) * N <= sum:
        while start <= end:
            mid = (start + end) // 2

    else:
        # 최저*N > sum
