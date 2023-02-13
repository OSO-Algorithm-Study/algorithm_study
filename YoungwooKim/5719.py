import sys, heapq
from collections import deque

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
INF = int(1e9)

def dijkstra():
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        dist, now = heapq.heappop(heap)

        if (distance[now] < dist):
            continue

        for i in graph[now]:
            cost = dist + graph[now][i]
            if (cost < distance[i]):
                distance[i] = cost
                heapq.heappush(heap, (cost, i))

def bfs():
    q = deque()
    q.append(end)

    while q:
        v = q.popleft()

        if (start == v):
            continue

        for prev_v, prev_c in r_graph[v]:
            if (prev_c + distance[prev_v] == distance[v]):
                if ((prev_v, v) not in remove_list):
                    remove_list.append((prev_v, v))
                    q.append(prev_v)

while True:
        n, m = map(int, input().split())
        if (n == m == 0):
            break

        start, end = map(int, input().split())
        graph = [dict() for _ in range(n)]
        r_graph = [[] for _ in range(n)]    # 경로 추적을 위해 역순 저장
        distance = [INF] * n

        for _ in range(m):
            u, v, p = map(int, input().split())
            graph[u][v] = p
            r_graph[v].append((u, p))

        dijkstra()

        remove_list = []
        bfs()

        for x, y in remove_list:
            del graph[x][y]

        distance = [INF] * n
        dijkstra()

        if (distance[end] == INF):
            print(-1)
        else:
            print(distance[end])
