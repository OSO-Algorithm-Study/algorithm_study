from heapq import heappush, heappop

def solution(n, paths, gates, summits):
    answer = []
    
    routes = [[] for _ in range(n+1)]
    
    for p in paths:
        routes[p[0]].append([p[1], p[2]])
        routes[p[1]].append([p[0], p[2]])
        
    # print(routes)
#   [[], [[3, 10], [4, 20]], [[3, 4], [4, 6]], [[1, 10], [2, 4], [5, 20]], [[1, 20], [2, 6], [5, 6]]]

    q = []
    visited = [10000001] * (n + 1)
    
    for i in range(len(gates)):
        heappush(q, (0, gates[i])) # distance / gate
        visited[gates[i]] = 0
    
    
    
    while q:
        intensity, node = heappop(q)
        
        if node in summits :
            answer.append([intensity, node])
            continue
            
        for route in routes[node]:
            next_node = route[0]
            next_intensity = route[1]

            max_intensity = max(intensity, next_intensity)

            if max_intensity < visited[next_node]:
                heappush(q, (max_intensity, next_node))
                visited[next_node] = max_intensity
    
    print(answer)
    
    return answer


n = 5
paths = [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]]
gates = [1, 2]
summits = [5]
result = [5, 6]

output = solution(n, paths, gates, summits)
print(output)