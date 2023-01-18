# 게임개발
import sys
from collections import deque 

n = int(sys.stdin.readline())
time = [0] * (n + 1)
indegree = [0] * (n + 1)
graph = [[] for _ in range(n+1)]


for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    graph[i].append(temp)
    time[i+1] = temp[0]
    
    for j in temp[1:]:
        if j == -1:
            break
        indegree[i+1] += 1
         

# 순서대로 내려오면서 index 0 이 아닐경우에는 
# 앞에 걸리는 시간을 + 해주면서 리스트에 저장
# 숫자가 -1일 경우 종료시키기 
def topology_sort():
    result = []
    q = deque()
    
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        now = q.popleft
        result.append(now)
        
        for i in range(len(graph[now])):
            
        
            