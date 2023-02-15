# 예산
import sys

n = int(sys.stdin.readline())
req = list(map(int, sys.stdin.readline().split()))
budget = int(sys.stdin.readline())

req.sort()

chk_sum = 0  # 최소값부터 더함
rest = budget # (budget - chksum)

if (sum(req) <= rest):
    print(req[-1])

elif ((req[0] >= rest) or ((req[0] + req[1]) >= budget)):
    print(rest // len(req))

else:
    for i in range(len(req)):
        chk_sum += req[i]
        rest -= req[i]
        
        if (rest // (len(req) - (i+1)) >= req[i+1]):
            continue
        else:
            print(rest // (len(req) - (i+1)))
            break
            
