from collections import deque

def solution(n, roads, sources, destination):
    global maps
    answer = []
    maps = [[] for _ in range(n + 1)]

    for i in range(len(roads)):
        first = roads[i][0]
        second = roads[i][1]
        
        maps[first].append(second)
        maps[second].append(first)
    
    # print(maps)
    
    answer = [0] * (len(sources))
    visited = [0] * (n + 1)
    
    ans = bfs(destination, sources, visited, answer)
    
    result = []
    for temp in sources:
        res = visited[temp]
        
        if res == 0:
            result.append(-1)
        elif res == -1:
            result.append(0)
        else:
            result.append(res)
        
    # print(result)
    
    # print(ans)
    
    return result

def bfs(dest, sources, visited, answer):
    queue = deque()
    count = 0
    queue.append([dest, count])
    visited[dest] = -1
    
    while (queue):
        temp = queue.popleft()
        dest = temp[0]
        count = temp[1] 
            
        for i in range(len(maps[dest])):
            if visited[maps[dest][i]] == 0:
                visited[maps[dest][i]] = count + 1
                queue.append([maps[dest][i], (count+1)])
    
    return visited
        
        
    