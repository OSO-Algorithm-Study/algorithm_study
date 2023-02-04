# 최단경로
import sys 
import heapq 

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
INF = 1e9

graph = [[] for _ in range(v + 1)]
for i in range(e):
    now, there, cost = map(int, sys.stdin.readline().split())
    graph[now].append((there, cost))


distance = [INF] * (v + 1)

def dijkstra(start):
    q = []
    
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, there = heapq.heappop(q)
        if distance[there] < dist:
            continue 
        for i in graph[there]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
dijkstra(k)

for i in range(1, len(distance)):
    if (distance[i] == INF):
        print("INF")
        continue
    print(distance[i])