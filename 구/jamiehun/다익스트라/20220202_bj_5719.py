# DFS + 다익스트라

import sys
from collections import heapq
INF = 1e9

# dfs로 그래프 파악
def dfs(graph, v, cost, count):
    if count == 0:
        temp = []
        
    temp.append(v)
    count += 1
    
    for i in graph[v]:
        if i[0] == d:
            cost += i[1]
            temp.append(i[0])
            visited.append(temp)
            total_cost.append(cost)
            return temp
        
        cost += i[1]
        dfs(graph, i[0], cost, count)

# 다익스트라로 최단거리 파악 
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue 
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


while True :
    n, m = map(int, sys.stdin.readline().split()) # n = 장소의 수 / m = 도로의 수
    s, d = map(int, sys.stdin.readline().split()) # s = 시작점 / d = 도착지점
    graph = []
    total_cost = []
    visited = []
    distance = [INF] * (n + 1)

    for _ in range(m):
        u, v, p = map(int, sys.stdin.readline().split())
        graph[u].append((v, p)) # v는 목적지, p는 cost 
        




        
