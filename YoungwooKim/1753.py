import sys, heapq

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v)) # 가중치, 간선 순으로 대입

INF = int(1e9)
distance = [INF] * (V + 1)
distance[start] = 0

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[0]
            if (cost < distance[i[1]]):
                distance[i[1]] = cost
                heapq.heappush(heap, (cost, i[1]))  # 최소 힙 구조, 가중치가 최소인 간선 선택

dijkstra(start)

for j in range(1, V + 1):
    if distance[j] == INF:
        print("INF")
    else:
        print(distance[j])

# 가중치가 최소인 간선을 택하기 위해서는 정렬이 필요하다. 단순 선택 정렬의 경우 O(n^2), 힙 정렬의 경우 O(nlogn)