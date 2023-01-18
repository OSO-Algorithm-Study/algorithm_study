import sys 

c = int(sys.stdin.readline())
n = int(sys.stdin.readline())
c_list = [[] for _ in range(c + 1)]

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    c_list[a].append(b)
    c_list[b].append(a)
    
visited = [False] * (c + 1)


def dfs(c_list, v, visited):
    visited[v] = True
    
    for i in c_list[v]:
        if not visited[i]:
            dfs(c_list, i, visited)
            
dfs(c_list, 1, visited)

cnt = 0
for i in visited:
    if i == True:
        cnt += 1

print(cnt-1)
        