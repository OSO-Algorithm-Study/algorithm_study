import sys 

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
visited = [False] * n
p.sort()
count = 0

for i in range(n-1):
    if p[i] == p[i+1] and visited[i] != True:
        visited[i] = True
        visited[i+1] = True
        count += 1 

if n == 1:
    total = 0 
elif (count * 2) == n :
    total = 0 
else:
    total = n - (2*count) - 1

print(total)