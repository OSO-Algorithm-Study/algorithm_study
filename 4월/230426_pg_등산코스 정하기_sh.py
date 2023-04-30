# 답안참고 : https://hz25.tistory.com/6 


from collections import defaultdict
from heapq import heappush, heappop
def solution(n, paths, gates, summits):
    def get_shortest_path():
        q = []
        visited = [10000001] * (n + 1)

        for i in gates:
            heappush(q, (0, i)) # distance / gate
            visited[i] = 0

        while q:
            intensity, node = heappop(q)

            if node in summits_set or intensity > visited[node]:
                continue

            for next_intensity, next_node in routes[node]:
                max_intensity = max(intensity, next_intensity)

                if max_intensity < visited[next_node]:
                    visited[next_node] = max_intensity
                    heappush(q, (max_intensity, next_node))
        
        min_intensity = [0, 10000001]
        
        for s in summits:
            if visited[s] < min_intensity[1]:
                min_intensity[0] = s
                min_intensity[1] = visited[s]
        
        return min_intensity
        
    
    summits.sort()
    summits_set = set(summits)
    
    routes = defaultdict(list)
    
    for i, j, k in paths:
        routes[i].append((k, j))
        routes[j].append((k, i))
    
    return get_shortest_path()
        
#     # print(routes)
#     	# defaultdict(<class 'list'>, {1: [[2, 5], [4, 1]], 2: [[1, 5], [3, 1], [6, 7]], 4: [[1, 1], [5, 1]], 3: [[2, 1]], 6: [[2, 7], [5, 1], [7, 1]], 5: [[4, 1], [6, 1]], 7: [[6, 1]]})


