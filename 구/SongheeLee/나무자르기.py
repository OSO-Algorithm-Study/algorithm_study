'''
4 7
20 15 10 17
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
logs = list(map(int, input().split()))

logs.sort()

if N == 1:
    print(logs[0]-M)

else: 
    logs.sort()
    start = logs[0]
    end = logs[-1]

    while(start <= end):
        left = 0
        mid = (start + end)//2
        for log in logs:
            if log > mid:
                left += (log - mid)
        if left >= M:
            start = mid + 1

        else:
            end = mid - 1

    answer = end

    print (answer)
