# bfs로 푸는 방법

import sys 
from collections import deque

cnt = 0

def bfs(x):
    global cnt 
    q = deque([x])
    visited[x] = True 
    
    while q:
        temp = q.popleft()
        
        if visited[temp] == False:
            visited[temp] = True
            cnt += 1 
        
        for i in c_list[temp]:
            if visited[i] == False:
                q.append(i)
                        
            


c = int(sys.stdin.readline())
n = int(sys.stdin.readline())
c_list = [[] for _ in range(c + 1)]

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    c_list[a].append(b)
    c_list[b].append(a)
    
visited = [False] * (c + 1)

bfs(1)

print(cnt)