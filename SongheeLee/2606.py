import sys
input = sys.stdin.readline

def dfs(start):
    for i in graph[start]:
        visited[start] = True
        if not visited[i]:              # if visited[node] == False:
            dfs(i)

if __name__ == "__main__":
    node = int(input())
    line = int(input())

    graph = [[] for _ in range(node+1)]

    for _ in range(line):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # for i in range(node+1):
    #     graph[i].sort()

    visited = [False]*(node+1)

    dfs(1)

    count = 0

    for i in visited:
        if i == True:
            count += 1
        
    print(count-1)