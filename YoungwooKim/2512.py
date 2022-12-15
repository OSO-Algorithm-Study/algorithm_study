import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N = int(input())

budget_list = list(map(int, input().split()))
budget_list.sort()

tot = int(input())

if tot >= sum(budget_list):
    print(budget_list[-1])

elif tot <= budget_list[0] * N:
    print(tot // N)
    
else:
    start = budget_list[0]
    end = budget_list[-1]
    
    while(start <= end):
        res = 0
        mid = (start + end) // 2
        if start == mid:
            break
        for budget in budget_list:
            if budget <= mid:
                res += budget
            else:
                res += mid
        if res > tot:
            end = mid
        else:
            start = mid

    print(mid)