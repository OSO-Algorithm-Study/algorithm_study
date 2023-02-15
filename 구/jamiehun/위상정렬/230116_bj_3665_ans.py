from collections import deque
import sys 

t = int(sys.stdin.readline())
answer = []

for i in range(t):
    n = int(sys.stdin.readline())
    
    graph = [[] for _ in range(n + 1)]
    inDegree = [0 for _ in range(n + 1)]
    queue = deque()

    
    team = list(map(int, sys.stdin.readline().split()))
    
    for j in range(n - 1):
        for k in range(j + 1, n):
            graph[team[j]].append(team[k])
            inDegree[team[k]] += 1
    
    m = int(sys.stdin.readline())
    
    if (m == 0):
        new_list = [0] + team
        answer.append(new_list)
        continue
    flag = False
    
    for j in range(m):

        first, second = map(int, sys.stdin.readline().split())
        
        if flag != "IMPOSSIBLE":
            for k in graph[second]:
                if k == first:
                    graph[second].remove(first)
                    inDegree[first] -= 1
                    graph[first].append(second)
                    inDegree[second] += 1
                    flag = True
                
        if flag == False:
            flag = "IMPOSSIBLE"
        
    if flag == "IMPOSSIBLE":
        answer.append("IMPOSSIBLE") 
        continue
    
        
    new_list =[0] * (n + 1)            
    # for i in range(len(team)):
    #     idx = inDegree[i+1]
    #     new_list[idx] = team[i]
    
    temp = team.copy()
    temp.sort()
    for i in range(len(inDegree)):
        if i == 0:
            continue
        
        if inDegree[i] == inDegree[i-1]:
            answer.append("IMPOSSIBLE")
            continue 
        
        idx = inDegree[i] + 1 
        new_list[i] = temp[idx - 1]
    
    
    answer.append(new_list)
        
for temp in answer:
    if temp == "IMPOSSIBLE":
        print("IMPOSSIBLE")
    else:
        for i in range(len(temp)):
            if i == 0:
                continue
            else:
                print(temp[i], end = " ")
        print()