import sys, heapq

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

while True:
    try:
        n, m = map(int, input())
        if (n == m == 0):
            EOFError

        start, end = map(int, input())
        graph = [[] for _ in range(n)]
        heap = []
        INF = 1e9

        for _ in range(m):
            u, v, p = map(int, input())
            graph[u] = (p, v)

        distance = [INF] * (n)
        distance[start] = 0

        heapq.heappush(heap, graph[start])

        while heap:
            cost, now = heapq.heappop(heap)
            distance[now] 
        

    except:
        break
