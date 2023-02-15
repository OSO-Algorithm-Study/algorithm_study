'''
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
'''

import sys
import heapq
input = sys.stdin.readline

def Dijkstra(Graph, start, N):
    Dist = [float('INF')] * (N+1)  # start로 부터의 거리 값을 저장하기 위함
    Dist[start] = 0 # 시작 값은 0이어야 함
    Q = []
    heapq.heappush(Q, [Dist[start], start]) # 시작 노드부터 탐색 시작 하기 위함.
    
    while Q: # queue에 남아 있는 노드가 없으면 끝
        curr_dist, curr_dest = heapq.heappop(Q)  # 탐색 할 노드, 거리를 가져옴.
        if Dist[curr_dest] < curr_dist: # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue

        for next_dest, next_dist in Graph[curr_dest]:
            distance = curr_dist + next_dist # 해당 노드를 거쳐 갈 때 거리
            if distance < Dist[next_dest]: # 알고 있는 거리 보다 작으면 갱신
                Dist[next_dest] = distance
                heapq.heappush(Q, [distance, next_dest]) # 다음 인접 거리를 계산 하기 위해 큐에 삽입

    return Dist


N, M = map(int, input().split()) # N: 노드의 개수, M: 간선의 개수
start = int(input()) # 시작 노드
Graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    Graph[u].append((v, w))

Dist = Dijkstra(Graph, start, N)

for i in range(1, N+1):
    print("INF" if Dist[i] == float('INF') else Dist[i])