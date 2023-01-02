import sys
input = sys.stdin.readline 

n, m = map(int ,input().split())
video = list(map(int, input().split()))

vm = max(video)
start = vm 
end = sum(video)

res = 10 ** 9

while (start <= end):
    mid = (start + end) // 2
    cnt = 1
    tmp = 0
    
    for i in range(n):
        # 블루레이에 비디오를 더 넣을 수 있다면
        if(tmp + video[i] <= mid):
            tmp += video[i]
        else:
            cnt += 1
            tmp = video[i] # 여기서부터 tmp 다시 시작 
    
        if (cnt > m): # 나눌 수 있는 값보다 더 많이 나눈 경우
            break
        
    if (cnt > m):
        start = mid + 1
    else:
        end = mid - 1
        if (mid >= vm): # video 리스트의 최대값보다 클 경우에만 res값 갱신
            res = min(res, mid)


print(res)
        