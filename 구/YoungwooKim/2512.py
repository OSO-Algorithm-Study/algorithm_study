import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N = int(input())

budget_list = list(map(int, input().split()))
budget_list.sort()

tot = int(input())

# 모든 요청이 배정될 수 있는 경우
if tot >= sum(budget_list):
    print(budget_list[-1])

# 모든 요청이 상한액으로 배정되어야 할 경우
elif tot <= budget_list[0] * N:
    print(tot // N)

else:
    start = budget_list[0]
    end = budget_list[-1]
    
    while(start <= end):
        res = 0
        mid = (start + end) // 2
        
        for budget in budget_list:
            if (budget <= mid):
                res += budget
            else:
                res += mid
        if (res > tot):
            end = mid - 1
        else:
            start = mid + 1

    print(end)

    #         if (res > tot):
    #         end = mid - 1
    #     else:
    #         ans = mid
    #         start = mid + 1

    # print(ans)