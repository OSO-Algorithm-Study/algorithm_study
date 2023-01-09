import sys
input = sys.stdin.readline


K, N = map(int, input().split())

cables = []

for _ in range (K):
    cables.append(int(input()))

cables.sort()

start, end = 1, cables[-1]
count, ans = 0, 0


while(start<=end):
    mid = (start+end)//2
    count = 0
    
    for i in range(K):
        count += cables[i] // mid
    
    if count < N:
        end = mid - 1
    
    elif count >= N:
        start = mid + 1
        ans = max(ans, mid)

print(ans)