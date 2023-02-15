import sys

# k : 랜선의 개수, n : 필요한 랜선의 개수
k, n = map(int, sys.stdin.readline().split())
len_list = []

for _ in range(k):
    len_list.append(int(sys.stdin.readline()))
    
start = 0
end = max(len_list)
result = 0

while start <= end:
    mid = (start + end) // 2
    if mid == 0:
        mid = 1
    cnt = 0
    
    for i in len_list:
        while i >= mid:
           i -= mid
           cnt += 1 
    
    if cnt < n:
        end = mid - 1 
    
    elif cnt >= n:
        start = mid + 1 
        
        result = max(mid, result)


print(result)

