# 예산
import sys

n = int(sys.stdin.readline())
req = list(map(int, sys.stdin.readline().split()))
budget = int(sys.stdin.readline())

req.sort()

# budget이 충분할 경우
if (sum(req) <= budget):
    print(req[-1])
    
# budget이 최소값에도 못 미칠 경우
elif (budget < req[0]):
    print(budget // n)
    
# budget을 나눈 값이 최소값에도 못 미칠 경우
elif (budget // n <= req[0]):
    print(budget // n)
    
# 정상적인 경우 
else:    
    start = req[0]
    end = req[-1]
    
    while (start < end):
        
        mid = (start + end) // 2
        if (mid == start or mid == end):
            break
        
        rest = 0
        
        for i in range(len(req)):
            if (req[i] >= mid):
                rest += mid
            else:
                rest += req[i] 
        
        if (rest == budget):
            break
        
        elif (rest > budget):
            end = mid 
        
        else:
            start = mid
    
    print(mid)