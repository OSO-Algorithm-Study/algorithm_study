import sys 
n, m = map(int, sys.stdin.readline().split())

lectures = list(map(int, sys.stdin.readline().split()))

start = 0
end = 100000 * 10000


while start <= end:
    result = []
    mid = (start + end) // 2
    
    temp = 0
    for i in range(n):
        temp += lectures[i]
        
        if i != (n-1) and temp + lectures[i+1] > mid:
           result.append(temp)
           temp = 0
    
    if temp != 0:
        result.append(temp)
    
    cnt = len(result)
    
    if cnt > m:
        start = mid + 1
    
    else :
        end = mid - 1
            

print(max(result))
# print(result)